from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


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


class ResultInstance(models.Model):
	"""
	The result from the instance
	"""
	result_id = models.AutoField(primary_key=True)
	instance = models.OneToOneField('ConfigInstance', on_delete=CASCADE)


class StudentSet(models.Model):
	"""
	this is the set of student that we use to run algorithm
	"""


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
		return reverse("iGroup:update", kwargs={"slug":self.slug})


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
