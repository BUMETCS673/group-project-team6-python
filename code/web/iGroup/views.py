from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import InstanceCreationForm
from .models import Instance


# The iGroup system
@login_required(login_url="/login")
def index(request):
	"""index page of the iGroup, show all the instances"""
	# get all instance relate to the logged in instructor
	current_instructor = request.user
	instances = Instance.objects.filter(instructor=current_instructor)
	#print(instances)

	return render(request, 'iGroup/home.html', {})


@login_required(login_url="/login")
def create_instance(request):
	"""create a new instance"""
	if request.method == 'POST':
		form = InstanceCreationForm(request.POST)
	# if form.is_valid():
	#	config = form.save()
	#	login(request, user)
	#	return redirect('home')
	# return redirect('')
	else:
		form = InstanceCreationForm()
	# print(dir(form))
	return render(request, 'iGroup/instance_create.html', {'form': form})


@login_required(login_url="/login")
def create_survey(request):
	"""create a new survey from form"""

	return


@login_required(login_url="/login")
def update_survey(request, id=None):
	"""update a survey"""
	return
