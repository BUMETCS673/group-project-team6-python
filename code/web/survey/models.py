from django.db import models
from django.db.models import CASCADE


# Create your models here.

# survey
class Survey(models.Model):
	"""
	Survey model
	"""
	survey_id = models.AutoField(primary_key=True)
	survey_name = models.CharField(max_length=20)
	num_question = models.IntegerField()
	active = models.BooleanField()
	send_survey = models.BooleanField()


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
	question_index = models.IntegerField()
	question_name = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	weight = models.IntegerField()
	survey = models.ForeignKey(Survey, on_delete=CASCADE)


class Choice(models.Model):
	"""
	choice field
	"""
	choice_index = models.IntegerField() # the position of the choice
	choice_name = models.CharField(max_length=50)
	question = models.ForeignKey(Question, on_delete=CASCADE)


# answer sheet
class AnswerSheet(models.Model):
	"""
	Answer sheet
	"""
	answer_sheet_id = models.AutoField(primary_key=True)
	survey = models.ForeignKey(Survey, on_delete=CASCADE)
	student = None  # should link to student


# generic answer
class Answer(models.Model):
	"""
	abstract model answer
	"""
	answer_id = models.AutoField(primary_key=True)
	answer_sheet = models.ForeignKey(AnswerSheet, on_delete=CASCADE)
	answer_type = models.CharField(max_length=50)
	question = models.ForeignKey(Question, on_delete=CASCADE)
