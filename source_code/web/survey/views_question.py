from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import QuestionCreationForm
from .models import Survey, Question


@login_required(login_url="/login")
def question_list(request, survey_id=None):
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey,
	                               survey_id=survey_id,
	                               instance__instructor=current_instructor)
	question_set = survey_obj.get_questions_set()
	context = {
		'question_set': question_set
	}

	return render(request, 'survey/partials/question_list.html', context)


@login_required(login_url="/login")
def add_question(request, survey_id=None):
	"""add question to the survey"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	question_set = survey_obj.get_questions_set()
	if not survey_obj.modify:
		# survey has been locked
		return  # not allowed response
	num_questions = len(question_set)
	if request.method == "POST":
		# create question
		question_form = QuestionCreationForm(request.POST, survey=survey_obj)
		if question_form.is_valid():
			question_obj = question_form.save(commit=False)
			question_obj.survey = survey_obj
			question_obj.question_index = num_questions + 1
			question_obj.save()
			return redirect('survey:survey_index', survey_id=survey_obj.survey_id)
	else:
		# GET
		question_form = QuestionCreationForm(survey=survey_obj)
	context = {
		'question_form': question_form,
		'survey_obj': survey_obj
	}
	return render(request, 'survey/question_form.html', context)


@login_required(login_url="/login")
def edit_question(request, survey_id=None, question_id=None):
	"""edit question in the survey"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	question_obj = get_object_or_404(Question, survey=survey_obj, question_id=question_id)

	if request.method == "POST" and survey_obj.modify:
		# modify question if the survey is not locked
		question_form = QuestionCreationForm(request.POST, instance=question_obj,survey=survey_obj)
		if question_form.is_valid():
			question_form.save()
			context = {
				'survey_obj': survey_obj,

			}
			return render(request, 'survey/survey_index.html', context)
	else:
		# GET

		question_form = QuestionCreationForm(instance=question_obj, survey=survey_obj)

	context = {
		'question_form': question_form,
		'question_obj': question_obj,
		'modify': survey_obj.modify,
		'survey_obj': survey_obj
	}
	return render(request, 'survey/question_form.html', context)


@login_required(login_url="/login")
def remove_question():
	pass
