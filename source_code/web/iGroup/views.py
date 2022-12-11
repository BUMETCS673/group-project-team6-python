from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import InstanceCreationForm, InstructorParameterForm
from .models import Instance, ConfigInstance
from survey.models import Survey
from .utils import run_algorithm, save_result

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
def config_instance(request, slug=None):
	"""Instructor config parameter for this instance"""
	current_instructor = request.user
	instance = get_object_or_404(Instance, slug=slug)

	if instance.instructor != current_instructor:
		raise Http404('deny')  # need to change in future

	survey = get_object_or_404(Survey, instance=instance)  # need one survey

	if request.method == 'POST':
		form = InstructorParameterForm(request.POST)
		if form.is_valid():
			config_instance_object = form.save(commit=False)
			config_instance_object.instance = instance
			config_instance_object.survey = survey
			config_instance_object.instructor = current_instructor
			config_instance_object.save()

			result = run_algorithm(config_instance_obj=config_instance_object,
			                       instance_obj=instance)
			# save result
			save_result(config_instance_obj=config_instance_object,
			            result=result)

			return redirect('iGroup:home')


	else:
		form = InstructorParameterForm()

	context = {
		'form': form
	}
	return render(request, 'iGroup/config.html', context)


@login_required(login_url="/login")
def delete_instance(request, slug):
	"""delete this instance"""
	current_instructor = request.user
	instance = get_object_or_404(Instance, slug=slug)

	if instance.instructor != current_instructor:
		raise Http404('deny')  # need to change in future

	instance.delete()
	return redirect('iGroup:home')


### show run result
@login_required(login_url="/login")
def list_config(request, slug):
	"""show all run configuration of an instance"""
	# assume get only
	current_instructor = request.user
	instance = get_object_or_404(Instance,
	                             instructor=current_instructor,
	                             slug=slug)
	# all the run configurations of this instance
	config_set = instance.get_configure_instance_set()
	context = {
		"config_set": config_set,
		"instance": instance
	}

	return render(request, 'iGroup/config_list.html', context)


@login_required(login_url="/login")
def detail_config(request, slug, config_id):
	"""show detailed run configuration of an instance"""
	# assume get only
	current_instructor = request.user
	instance = get_object_or_404(Instance,
	                             instructor=current_instructor,
	                             slug=slug)
	# all the run configurations of this instance
	config_obj = get_object_or_404(ConfigInstance,
	                               instance=instance,
	                               config_id=config_id)

	context = {
		"config_obj": config_obj
	}

	return render(request, 'iGroup/config_detail.html', context)


@login_required(login_url="/login")
def detail_result(request, slug, config_id):
	"""show result of group formation"""
	current_instructor = request.user
	instance = get_object_or_404(Instance,
	                             instructor=current_instructor,
	                             slug=slug)
	# all the run configurations of this instance
	config_obj = get_object_or_404(ConfigInstance,
	                               instance=instance,
	                               config_id=config_id)

	# get the result teams
	team_obj_set = config_obj.get_result_teams()

	# init result
	result = list()
	for team_obj in team_obj_set:
		"""pack team data"""
		team_data = dict()
		team_data['team_index'] = team_obj.team_index
		team_data['team_size'] = team_obj.team_size
		team_data['team_name'] = team_obj.team_name
		team_data['total_score'] = team_obj.total_score

		"""pack result question data"""
		all_result_questions = team_obj.get_question_scores()
		questions_score = list()
		for result_question in all_result_questions:
			"""pack result question data"""
			question_data = dict()
			question_data['question_name'] = result_question.get_question_name()
			question_data['question_score'] = result_question.question_score
			question_data['question_weight'] = result_question.question_weight
			question_data['question_type'] = result_question.question_type
			questions_score.append(question_data)
		team_data['result_questions'] = questions_score

		"""pack student data"""
		all_students = team_obj.get_student_team_set()
		team_data['student_set'] = all_students

		# update results
		result.append(team_data)

	context = {
		"teams_result": result,
		"instance":instance
	}

	return render(request, 'iGroup/result_detail.html', context)
