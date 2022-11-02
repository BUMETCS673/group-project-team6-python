from django import forms
from .models import ConfigInstance, Instance, ResultInstance
from survey.models import Survey  # import survey
from django.forms import ModelForm


class InstanceCreationForm(ModelForm):
	"""Instance form to create an instance"""

	class Meta:
		model = Instance
		fields = ("instance_name",)

	def __init__(self, instructor, *args, **kwargs):
		self.instructor = instructor
		super().__init__(*args, **kwargs)

	def clean(self):
		"""form validation"""
		data = self.cleaned_data
		instance_name = data.get('instance_name')
		current_instructor = self.instructor
		# find the duplication instances within current user's all instance
		instances = Instance.objects.filter(instructor=current_instructor)
		qs = instances.filter(instance_name__contains=instance_name)
		if qs.exists():
			self.add_error("instance_name", f'{instance_name} is already in use')
		return data


class SurveyCreationForm(ModelForm):
	"""Survey from to create n survey"""

	class Meta:
		model = Survey
		fields = ('survey_name',)
