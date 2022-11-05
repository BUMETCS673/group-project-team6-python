from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import SurveyCreationForm, QuestionCreationForm, \
	OptionCreationForm, QuestionCreationFormSet, OptionCreationFormSet
from django.forms.models import modelformset_factory
from iGroup.models import Instance
from .models import Survey, Question


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
		context = {
			'survey_form': survey_form,
			'question_formset': question_formset,
		}
		return render(request, "survey/survey_create.html", context)
	else:
		survey_form = SurveyCreationForm(instance=survey)
		questions = survey.get_questions_set()
		question_formset = QuestionCreationFormSet(queryset=questions)

	context = {
		'survey_form': survey_form,
		'question_formset': question_formset,
	}
	return render(request, "survey/survey_create.html", context)


@login_required(login_url="/login")
def create_update_options(request, question_id=None):
	"""create or update option of a given question"""
	current_instructor = request.user
	question_obj = get_object_or_404(Question, question_id=question_id)
	instance_obj = question_obj.survey.instance
	if question_obj.survey.instance.instructor != current_instructor:
		raise Http404  # not allowed to modify

	options = question_obj.get_options_set()

	if request.method == 'POST':
		option_formset = OptionCreationFormSet(request.POST, queryset=options)
		option_index = 0
		if option_formset.is_valid():
			for option_form in option_formset:
				option = option_form.save(commit=False)
				option.question = question_obj
				option.choice_index = option_index
				option.save()
		return redirect('survey:survey_create_update', instance_slug=instance_obj.slug)
	else:
		option_formset = OptionCreationFormSet(queryset=options)

	context = {
		'option_formset': option_formset,
		'current_question': question_obj,

	}

	print("okkkk")
	return render(request, "survey/option_create.html", context)


#delete options
@login_required(login_url="/login")
def delete_options(request,question_id=None):
	current_instructor = request.user
	question_obj = get_object_or_404(Question, question_id=question_id)
	instance_obj = question_obj.survey.instance
	if question_obj.survey.instance.instructor != current_instructor:
		raise Http404  # not allowed to modify

	options = question_obj.get_options_set()

	options.delete()
	return redirect('survey:survey_create_update', instance_slug=instance_obj.slug)



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
