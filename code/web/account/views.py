from django import views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, View
from .forms import InstructorCreationForm
from .models import Instructor
from django.contrib.auth import authenticate, login, logout


def home(request):
	render(request, 'welcome.html')


def register(request):
	if request.method == 'POST':
		form = InstructorCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('welcome')
	else:
		form = InstructorCreationForm()

	return render(request, 'registration/register.html', {'form': form})
