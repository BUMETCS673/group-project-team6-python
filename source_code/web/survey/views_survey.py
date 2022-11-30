from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, Http404, get_object_or_404
from iGroup.models import Instance

from .forms import SurveyCreationForm
from .models import Survey


@login_required(login_url="/login")
def create_survey(request, instance_slug=None):
	"""create a new survey"""
	current_instructor = request.user
	instance_obj = get_object_or_404(Instance, instructor=current_instructor,
	                                 slug=instance_slug)  # report error, need to
	if Survey.objects.filter(instance=instance_obj, instance__instructor=current_instructor).exists():
		raise Http404
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
def get_survey_link(request, survey_id=None):
	"""lock the survey and send the survey"""
