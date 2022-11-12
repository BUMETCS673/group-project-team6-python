from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.urls import reverse


# Create your models here.

# survey
class Survey(models.Model):
	"""
	Survey model
	"""
	survey_id = models.AutoField(primary_key=True)
	survey_name = models.CharField(max_length=20)
	num_question = models.IntegerField(default=0)
	active = models.BooleanField(default=False)
	send_survey = models.BooleanField(default=False)
	instance = models.OneToOneField('iGroup.Instance', on_delete=CASCADE)

	def get_absolute_url(self):
		return reverse('survey:detail', kwargs={"survey_id": self.survey_id})

	def get_questions_set(self):
		"""get all question set to this survey"""
		return self.question_set.all()


# question

class Question(models.Model):
	"""
	Generic question model
	"""

	class QuestionType(models.TextChoices):
		"""
		the question types
		"""
		single_question = ("SINGLE", "Single choice")
		multiple_question = ("MULTIPLE", "Multiple choice")

	question_id = models.AutoField(primary_key=True)
	question_type = models.CharField(choices=QuestionType.choices, max_length=50)
	question_index = models.IntegerField()  # position in the survey
	question_name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	weight = models.IntegerField(default=0)
#	max_choice = models.IntegerField(default=1)
	survey = models.ForeignKey('Survey', on_delete=CASCADE)

	def get_absolute_url(self):
		return self.survey.get_absolute_url()

	def get_options_set(self):
		"""get all option to this question"""
		return self.option_set.all()

	def get_options_set_order_by_index(self):
		"""get all options to this question and order by their index value"""
		return self.option_set.all().order_by('choice_index')

	def get_options_name_order_by_index(self):
		""""""
		options_name = self.get_options_set_order_by_index().values('choice_name')
		return options_name


class Option(models.Model):
	"""
	choice field
	"""
	choice_index = models.IntegerField()  # the position of the choice
	choice_name = models.CharField(max_length=50)
	question = models.ForeignKey('Question', on_delete=CASCADE)

	def get_question_index(self):
		return self.question.question_index

	def __repr__(self):
		return self.choice_name

	def __str__(self):
		return self.choice_name


# answer sheet
class AnswerSheet(models.Model):
	"""
	Answer sheet
	"""
	answer_sheet_id = models.AutoField(primary_key=True)
	survey = models.ForeignKey('Survey', on_delete=CASCADE)
	student = models.ForeignKey('account.Student', on_delete=CASCADE)  # should link to student


# answer_single_choice = models.ManyToManyField('ChoiceSingle')
# answer_multiple_choice = models.ManyToManyField('ChoiceMultiple')


class ChoiceMultiple(models.Model):
	option = models.ForeignKey('Option', on_delete=CASCADE)
	rank = models.IntegerField(null=False)
	answer_sheet = models.ForeignKey('AnswerSheet', on_delete=CASCADE)

	def get_student(self):
		return self.answer_sheet.student

	def get_question_index(self):
		return self.option.get_question_index()

	def get_choice_index(self):
		return self.option.choice_index


class ChoiceSingle(models.Model):
	option = models.ForeignKey('Option', on_delete=CASCADE)
	answer_sheet = models.ForeignKey('AnswerSheet', on_delete=CASCADE)

	def get_student(self):
		return self.answer_sheet.student

	def get_question_index(self):
		return self.option.get_question_index()

	def get_choice_index(self):
		return self.option.choice_index
