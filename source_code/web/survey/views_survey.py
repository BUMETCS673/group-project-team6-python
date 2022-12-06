from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, Http404, get_object_or_404
from iGroup.models import Instance
from django.urls import reverse

from .forms import SurveyCreationForm, LockSurveyForm
from .models import Survey


@login_required(login_url="/login")
def create_survey(request, instance_slug=None):
	"""create a new survey"""
	current_instructor = request.user
	instance_obj = get_object_or_404(Instance, instructor=current_instructor,
	                                 slug=instance_slug)  # report error, need to
	if Survey.objects.filter(instance=instance_obj, instance__instructor=current_instructor).exists():
		raise Http404  # if already have one survey
	survey_form = SurveyCreationForm(request.POST or None)
	if survey_form.is_valid():
		survey_obj = survey_form.save(commit=False)
		survey_obj.instance = instance_obj
		survey_obj.save()
		# redirect to question page
		return redirect('survey:survey_index', survey_id=survey_obj.survey_id)
	context = {
		'survey_form': survey_form
	}
	return render(request, 'survey/create_survey.html', context)


@login_required(login_url="/login")
def edit_survey():
	pass


@login_required(login_url="/login")
def delete_survey():
	pass


@login_required(login_url="/login")
def survey_index(request, survey_id=None):
	"""show page of survey"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey,
	                               survey_id=survey_id,
	                               instance__instructor=current_instructor)
	context = {
		'survey_obj': survey_obj
	}
	return render(request, 'survey/survey_index.html', context)


@login_required(login_url="/login")
def lock_survey(request, survey_id=None):
	"""lock the survey """
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey,
	                               survey_id=survey_id,
	                               instance__instructor=current_instructor)
	if request.method == "POST":
		if not survey_obj.modify:
			# survey is already locked
			return redirect('survey:get_survey_link', survey_id=survey_id)
		form = LockSurveyForm(request.POST)
		if form.is_valid():
			modify = form.cleaned_data['lock_modify']
			survey_obj.modify = not modify
			survey_obj.save()
		return redirect('survey:get_survey_link', survey_id=survey_id)
	else:
		form = LockSurveyForm()
	context = {
		'form': form
	}
	if not survey_obj.modify:
		# if survey is locked
		return  # redirect to student link page
	return render(request, 'survey/survey_lock.html', context)


@login_required(login_url="/login")
def get_survey_link(request, survey_id=None):
	# get the survey link if locked, otherwise redirect to lock_survey page
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey,
	                               survey_id=survey_id,
	                               instance__instructor=current_instructor)
	if survey_obj.modify:
		# if the survey has been locked, get the survey link
		return redirect('survey:lock_survey', survey_id=survey_id)
	else:
		link = str(reverse('survey:survey_answer', kwargs={'survey_id': survey_id}))
		context = {
			'survey_link': link
		}
		return render(request, 'survey/survey_link.html', context)


@login_required(login_url="/login")
def view_survey(request, survey_id=None):
	"""view locked survey after lock the survey"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey,
	                               survey_id=survey_id,
	                               instance__instructor=current_instructor)
	if survey_obj.modify:
		# if allow to modify go to modify page
		return redirect('survey:question_list', survey_id=survey_id)
	return
