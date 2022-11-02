from django import forms
from .models import ConfigInstance, Instance, ResultInstance
from survey.models import Survey
from django.forms import ModelForm


class InstanceCreationForm(ModelForm):
	"""Instance form to create an instance"""

	class Meta:
		model = Instance
		fields = ("instance_name",)


class SurveyCreationForm(ModelForm):
	"""Survey from to create n survey"""

	class Meta:
		model = Survey
		fields = ('survey_name',)
