from django import forms
from .models import Instructor
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class InstructorCreationForm(UserCreationForm):
	"""Instructor user form to create user"""

	class Meta:
		model = Instructor
		fields = ("username", "email", "first_name", "last_name")


class InstructorChangeForm(UserChangeForm):
	"""Instructor user form to change user"""

	class Meta:
		model = Instructor
		fields = ("username", "email", "first_name", "last_name")
