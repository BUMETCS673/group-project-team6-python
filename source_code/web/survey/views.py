from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import SurveyCreationForm, QuestionCreationForm, \
	OptionCreationForm, QuestionCreationFormSet, OptionCreationFormSet
from django.forms.models import modelformset_factory
from iGroup.models import Instance
from .models import Survey


@login_required(login_url="/login")
def create_update_survey(request, instance_slug=None):
	"""create a new survey"""
	current_instructor = request.user
	instance_obj = get_object_or_404(Instance, instructor=current_instructor,
	                                 slug=instance_slug)  # report error, need to
	survey, created = Survey.objects.get_or_create(instance=instance_obj)

	if request.method == 'POST':
		survey_form = SurveyCreationForm(request.POST or None, instance=survey)
		questions = survey.get_questions_set()
		question_formset = QuestionCreationFormSet(request.POST or None, queryset=questions)
		if all([survey_form.is_valid(), question_formset.is_valid()]):
			survey = survey_form.save(commit=False)
			survey.save()
			question_index = 0
			for question_form in question_formset:
				question = question_form.save(commit=False)
				question.survey = survey
				question.question_index = question_index
				question.save()
				question_index += 1

		return redirect('iGroup:detail', slug=instance_slug)
	else:
		survey = Survey.objects.get(instance=instance_obj)
		survey_form = SurveyCreationForm(instance=survey)
		questions = survey.get_questions_set()
		question_formset = QuestionCreationFormSet(queryset=questions)

	context = {
		'survey_form': survey_form,
		'question_formset': question_formset,
	}
	return render(request, "survey/survey_create.html", context)


@login_required(login_url="/login")
def delete_survey(request, id=None):
	"""update a survey"""
	return


@login_required(login_url="/login")
def detail_survey(request):
	return None


def review(request):
	return None


def survey_lock(request):
	return None


def survey_response(request):
	return None
