from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import InstructorCreationForm
from .models import Instructor


class register(CreateView):
	form_class = InstructorCreationForm
	success_url = reverse_lazy("login")
	template_name = "registration/register.html"
