from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import InstanceCreationForm,InstructorParameterForm
from .models import Instance
from survey.models import Survey



# The iGroup system
@login_required(login_url="/login")
def index(request):
	"""index page of the iGroup, show all the instances"""
	# get all instance relate to the logged in instructor
	current_instructor = request.user
	instances = Instance.objects.filter(instructor=current_instructor)
	# pass data to index page(home)
	context = {
		"instances": instances,
		"current_instructor": current_instructor
	}
	return render(request, 'iGroup/home.html', context=context)


@login_required(login_url="/login")
def create_instance(request):
	"""create a new instance"""
	current_instructor = request.user
	if request.method == 'POST':
		# if post, input form and current instructor
		form = InstanceCreationForm(current_instructor, request.POST)
		if form.is_valid():
			# if the form is valid
			instance_object = form.save(commit=False)
			instance_object.instructor = current_instructor
			instance_object.save()
			# redirect back to index(home) page
			return redirect('iGroup:home')
	else:
		# if GET
		form = InstanceCreationForm(current_instructor)
	context = {
		"form": form
	}

	return render(request, 'iGroup/instance_create.html', context)


@login_required(login_url="/login")
def detail_instance(request, slug=None):
	"""detail page of a instance"""
	current_instructor = request.user
	instance = None
	if slug:
		instance = get_object_or_404(Instance, instructor=current_instructor, slug=slug)
	context = {
		"instance": instance
	}
	return render(request, 'iGroup/instance.html', context)


@login_required(login_url="/login")
def update_instance(request):
	return None


@login_required(login_url="/login")
def delete(request):
	return None


@login_required(login_url="/login")
def config_instance(request, slug=None):
	"""Instructor config parameter for this instance"""
	current_instructor = request.user
	instance = get_object_or_404(Instance, slug=slug)
	survey = get_object_or_404(Survey, instance=instance)  # need one survey

	if request.method == 'POST':
		form = InstructorParameterForm(request.POST)
		if form.is_valid():
			config_instance_object = form.save(commit=False)
			config_instance_object.instance = instance
			config_instance_object.survey = survey
			config_instance_object.instructor = current_instructor
			config_instance_object.save()


	else:
		form = InstructorParameterForm()

	context = {
		'form': form
	}
	return render(request, 'iGroup/config.html', context)

	return None