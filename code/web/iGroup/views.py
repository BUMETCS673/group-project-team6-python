from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import ConfigInstanceCreationForm


# The iGroup system
@login_required(login_url="/login")
def index(request):
	"""index page of the iGroup, show all the instances"""
	return render(request, 'iGroup/home.html', {})


def create_instance(request):
	"""create a new instance"""
	if request.method == 'POST':
		form = ConfigInstanceCreationForm(request.POST)
		#if form.is_valid():
		#	config = form.save()
		#	login(request, user)
		#	return redirect('home')
		#return redirect('')
	else:
		form = ConfigInstanceCreationForm()
	return render(request, 'iGroup/instance_create.html', {'form': form})

