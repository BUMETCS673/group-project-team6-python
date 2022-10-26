from django.db import models


class ConfigInstance(models.Model):
	"""
	The parameter for running the instance
	"""
	instructor = None # need to specifys


class ResultInstance(models.Model):
	"""
	The result from the instance
	"""
