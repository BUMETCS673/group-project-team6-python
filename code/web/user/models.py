from django.db import models


# Create your models here.
class Instructor(models.Model):
	"""
	this is the instructor model
	"""
	email = models.EmailField(max_length=256)
	name = models.CharField(max_length=256)
	password = models.CharField(max_length=256)


class Student(models.Model):
	"""
	this is the student model
	"""
	email = models.EmailField(max_length=256)
	name = models.CharField(max_length=256)
	course = models.CharField(max_length=256)
