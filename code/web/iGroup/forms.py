from django import forms
from .models import ConfigInstance
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ConfigInstanceCreationForm(ModelForm):
	"""Instance config form to create a instance config"""


	class Meta:
		model = ConfigInstance
		fields = ("max_num_pass", "num_group", "survey", )
