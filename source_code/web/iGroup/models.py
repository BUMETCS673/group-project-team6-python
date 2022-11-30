from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class Instance(models.Model):
	"""
	This is the instance page
	"""
	instance_id = models.AutoField(primary_key=True)
	instance_name = models.CharField(max_length=256)
	instructor = models.ForeignKey('account.Instructor', related_name="instances", on_delete=CASCADE)
	slug = models.SlugField(blank=True, null=True)  # for url slug

	def __str__(self):
		return self.instance_name

	def save(self, *args, **kwargs):
		"""override save method for add slug"""

		super().save(*args, **kwargs)

	def get_absolute_url(self):
		"""reverse url"""
		return reverse("iGroup:detail", kwargs={"slug": self.slug})

	def get_edit_url(self):
		"""get url for updating instance"""
		return reverse("iGroup:update", kwargs={"slug": self.slug})

	def get_configure_instance_set(self):
		"""get all results relate to this instance"""
		return self.configinstance_set.all()


class ConfigInstance(models.Model):
	"""
	The parameter for running the instance
	"""
	config_id = models.AutoField(primary_key=True)
	instance = models.ForeignKey('Instance', on_delete=CASCADE)
	instructor = models.ForeignKey('account.Instructor', on_delete=CASCADE)  # need to specify
	max_num_pass = models.IntegerField()
	survey = models.ForeignKey('survey.Survey', on_delete=CASCADE)
	num_group = models.IntegerField()

	def get_instance(self):
		"""get self instance"""
		return self.instance

	def get_survey(self):
		"""get survey"""
		return self.instance.survey

	def get_result_teams(self):
		"""get all result teams"""
		return self.resultteam_set.all()

	def __repr__(self):
		"""representation"""
		return self.config_id

	def __str__(self):
		rpr = f"Instance result {self.instance.instance_name}, id {self.config_id}"
		return rpr


class ResultTeam(models.Model):
	"""
	store the result team formation and its detail scores
	"""
	config_instance = models.ForeignKey(ConfigInstance, on_delete=CASCADE)
	team_index = models.IntegerField()
	team_name = models.CharField(max_length=256)
	team_size = models.IntegerField(default=0)
	total_score = models.FloatField()

	def get_question_scores(self):
		"""get all question scores"""
		return self.resultquestionscore_set.all()

	def get_student_team_set(self):
		"""get all student belong to this team"""
		return self.studentteam_set.all()



class StudentTeam(models.Model):
	"""
	this is the set of student belong to a team
	"""
	student = models.ForeignKey('account.Student', on_delete=CASCADE)
	result_team = models.ForeignKey(ResultTeam, on_delete=CASCADE)

	def __repr__(self):
		return self.student.email

	def __str__(self):
		return self.student.email


class ResultQuestionScore(models.Model):
	"""
	record result question score
	"""
	result_team = models.ForeignKey(ResultTeam, on_delete=CASCADE)
	question = models.ForeignKey('survey.Question', on_delete=CASCADE)
	question_type = models.CharField(max_length=256)
	question_weight = models.IntegerField()
	question_score = models.FloatField()

	def get_question_name(self):
		"""return question name"""
		return self.question.question_name


def slugify_instance_name(instance, save=False):
	"""function for slugify the instance name"""
	slug = slugify(instance.instance_name)
	# find the set of same slugify name
	instances = Instance.objects.filter(slug=slug).exclude(instance_id=instance.instance_id)
	if instances.exists():
		# generate new slug:
		slug = f'{slug}-{instances.count() + 1}'
	instance.slug = slug
	if save:
		instance.save()
	return instance


def instance_pre_save(sender, instance, *args, **kwargs):
	"""signal for pre save"""
	print('pre_save')
	if not instance.slug:
		# if first time create, not save
		slugify_instance_name(instance, save=False)


pre_save.connect(instance_pre_save, sender=Instance)


def instance_post_save(sender, instance, created, *args, **kwargs):
	"""signal for post save"""
	print("post save")
	if created:
		slugify_instance_name(instance, save=True)


post_save.connect(instance_post_save, sender=Instance)
