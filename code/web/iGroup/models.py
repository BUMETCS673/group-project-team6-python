from django.db import models
from django.db.models import CASCADE


class ConfigInstance(models.Model):
	"""
	The parameter for running the instance
	"""
	config_id = models.AutoField(primary_key=True)
	instance = models.OneToOneField('Instance', on_delete=CASCADE, null=True)
	instructor = models.ForeignKey('account.Instructor', on_delete=CASCADE)  # need to specify
	max_num_pass = models.IntegerField()
	survey = models.ForeignKey('survey.Survey', on_delete=CASCADE)
	num_group = models.IntegerField()


class ResultInstance(models.Model):
	"""
	The result from the instance
	"""
	result_id = models.AutoField(primary_key=True)
	instance = models.ForeignKey('Instance', on_delete=CASCADE)


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
	instructor = models.ForeignKey('account.Instructor',related_name="instances",on_delete=CASCADE)
	#survey = models.OneToOneField(Survey, on_delete=CASCADE, null=True)
