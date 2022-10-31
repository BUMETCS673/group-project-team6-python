from django.db import models
from account.models import Instructor, Student
from survey.models import Survey
from django.db.models import CASCADE


class ConfigInstance(models.Model):
	"""
	The parameter for running the instance
	"""
	instructor = models.ForeignKey(Instructor, on_delete=CASCADE)  # need to specify
	max_num_pass = models.IntegerField()
	survey = models.ForeignKey(Survey, on_delete=CASCADE)
	num_group = models.IntegerField()


class ResultInstance(models.Model):
	"""
	The result from the instance
	"""


class StudentSet(models.Model):
	"""
	this is the set of student that we use to run algorithm
	"""