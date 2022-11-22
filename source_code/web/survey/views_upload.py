import io

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Survey
from .utils import save_question_set, save_all_student_answer_set


@login_required(login_url="/login")
def upload_answers_csv(request, survey_id=None):
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	instance_slug = survey_obj.instance.slug
	context = {
		'survey_obj': survey_obj
	}
	if request.method == "GET":
		return render(request, 'survey/upload/upload_questions_csv.html', context)

	csv_file = request.FILES['csv_file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')

	question_set = csv_file.read().decode('utf-8-sig')
	io_string = io.StringIO(question_set)

	try:
		save_all_student_answer_set(io_string, survey_obj, request)
	except Exception as e:
		# raise exception if error occur
		return HttpResponse(str(e))

	context = {  # not used yet
		'survey_obj': survey_obj
	}
	return redirect('iGroup:detail', slug=instance_slug)


@require_http_methods(['POST'])
@login_required(login_url="/login")
def upload_questions_csv(request, survey_id=None):
	"""upload question set from csv file"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	context = {}
	if request.method == "GET":
		render(request, 'survey/upload/upload_questions_csv.html', context)

	csv_file = request.FILES['csv_file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')

	question_set = csv_file.read().decode('utf-8-sig')
	io_string = io.StringIO(question_set)
	total_saved, total_upload = save_question_set(io_string, survey_obj)

	context = {  # not used yet
		"total_saved": total_saved,
		"total_upload": total_upload,
		'survey_obj': survey_obj
	}
	return redirect('survey:survey_index', survey_id=survey_id)
