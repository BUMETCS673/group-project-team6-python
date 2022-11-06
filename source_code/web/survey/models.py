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
	survey = models.ForeignKey('Survey', on_delete=CASCADE)

	def get_absolute_url(self):
		return self.survey.get_absolute_url()

	def get_options_set(self):
		"""get all option to this question"""
		return self.option_set.all()


class Option(models.Model):
	"""
	choice field
	"""
	choice_index = models.IntegerField()  # the position of the choice
	choice_name = models.CharField(max_length=50)
	question = models.ForeignKey('Question', on_delete=CASCADE)


# answer sheet
class AnswerSheet(models.Model):
	"""
	Answer sheet
	"""
	answer_sheet_id = models.AutoField(primary_key=True)
	survey = models.ForeignKey('Survey', on_delete=CASCADE)
	student = models.ForeignKey('account.Instructor', on_delete=CASCADE)  # should link to student


# generic answer
class Answer(models.Model):
	"""
	 model answer
	"""
	answer_id = models.AutoField(primary_key=True)
	answer_index = models.IntegerField(default=None)
	answer_sheet = models.ForeignKey('AnswerSheet', on_delete=CASCADE)
	answer_type = models.CharField(max_length=50)
	question = models.ForeignKey('Question', on_delete=CASCADE)
	num_choice = models.IntegerField(default=0)


class AnswerChoice(models.Model):
	"""
	choice
	"""
	answer_choice_id = models.AutoField(primary_key = True)
	choice = models.ForeignKey(Option, on_delete=CASCADE)
	answer = models.ForeignKey(Answer, on_delete=CASCADE)
