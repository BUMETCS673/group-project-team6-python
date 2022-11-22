from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .forms import OptionCreationForm
from .models import Survey, Question, Option
from .utils import reorder


@login_required(login_url="/login")
def add_option(request, survey_id=None, question_id=None):
	"""add option for this question"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	question_obj = get_object_or_404(Question, survey=survey_obj, question_id=question_id)
	option_set = question_obj.get_options_set()
	num_option = len(option_set)
	if request.method == "POST":
		# create question
		option_form = OptionCreationForm(request.POST, question=question_obj)
		if option_form.is_valid():
			option_obj = option_form.save(commit=False)
			option_obj.question = question_obj
			option_obj.choice_index = num_option
			option_obj.save()
			print("done", option_obj.choice_index)
			return redirect('survey:option_list',
			                survey_id=survey_obj.survey_id,
			                question_id=question_obj.question_id)
		print("not done")
	else:
		# GET
		option_form = OptionCreationForm(question=question_obj)
	context = {
		'option_form': option_form
	}
	return render(request, 'survey/option_form.html', context)


@login_required(login_url="/login")
def option_list(request, survey_id=None, question_id=None):
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey,
	                               survey_id=survey_id,
	                               instance__instructor=current_instructor)
	question_obj = get_object_or_404(Question, survey=survey_obj, question_id=question_id)
	option_set = question_obj.get_options_set()
	context = {
		'option_set': option_set,
		'question_obj': question_obj,
		'survey_obj': survey_obj
	}

	return render(request, 'survey/partials/option_list.html', context)


@login_required(login_url="/login")
def option_sort(request, question_id=None):
	option_order = request.POST.getlist('option_order')
	print(option_order)
	current_instructor = request.user
	question_obj = get_object_or_404(Question,
	                                 question_id=question_id,
	                                 survey__instance__instructor=current_instructor)
	option_set = []
	for idx, option_pk in enumerate(option_order):
		option_obj = Option.objects.get(pk=option_pk,
		                                question=question_obj)
		print(option_obj)
		option_obj.choice_index = idx
		option_obj.save()
		option_set.append(option_obj)
	print(option_set)
	context = {
		'option_set': option_set,
		'question_obj': question_obj
	}
	return render(request, 'survey/partials/option_list.html', context)


@require_http_methods(['DELETE'])
@login_required(login_url="/login")
def delete_option(request, pk=None, question_id=None):
	current_instructor = request.user
	option_obj = Option.objects.get(pk=pk)
	question_obj = get_object_or_404(Question, question_id=question_id)
	if question_obj.survey.instance.instructor != current_instructor:
		raise Http404
	option_obj.delete()

	reorder(question_obj)

	options = question_obj.get_options_set()
	context = {
		'option_set': options
	}
	return render(request, 'survey/partials/option_list.html', context)
