from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import SurveyCreationForm, QuestionCreationForm, \
	OptionCreationForm, QuestionCreationFormSet, OptionCreationFormSet
from django.forms.models import modelformset_factory
from iGroup.models import Instance
from .models import Survey


@login_required(login_url="/login")
def create_survey(request, instance_slug=None):
	"""create a new survey"""
	current_instructor = request.user
	instance = get_object_or_404(Instance, instructor=current_instructor, slug=instance_slug)  # report error, need to
	# change

	if request.method == 'POST':
		survey_form = SurveyCreationForm(request.POST)
		question_formset = QuestionCreationFormSet(request.POST)
		if all([survey_form.is_valid(), question_formset.is_valid()]):
			survey = survey_form.save(commit=False)
			survey.instance = instance
			survey.save()
			for question_form in question_formset:
				print('q')
				question = question_form.save(commit=False)
				question.survey = survey
				question.save()
			print("good")
			return redirect('iGroup:home')
	else:
		# init new survey form
		survey_find = Survey.objects.filter(instance=instance)
		if survey_find.exists():
			survey = survey_find.get()
			survey_form = SurveyCreationForm(instance=survey)
			questions = survey.get_questions_set()
			question_formset = QuestionCreationFormSet(queryset=questions)
		else:
			survey_form = SurveyCreationForm()
			question_formset = QuestionCreationFormSet()

	context = {
		'survey_form': survey_form,
		'question_formset': question_formset,
	}
	return render(request, "survey/survey_create.html", context)


@login_required(login_url="/login")
def update_survey(request, id=None):
	"""update a survey"""

	return


@login_required(login_url="/login")
def delete_survey(request, id=None):
	"""update a survey"""
	return


@login_required(login_url="/login")
def detail_survey(request):
	return None


def survey_create_view(request):
	current_instructor = request.user
	form = SurveyCreationForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		survey = form.save(commit=False)
		survey
