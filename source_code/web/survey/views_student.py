from django.shortcuts import Http404
from account.models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import StudentCreationFrom,SurveyForm
from .models import Survey, AnswerSheet


@require_http_methods(['GET'])
@login_required(login_url="/login")
def student_list(request, survey_id=None):
	"""list all student answer this survey"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	all_responses = survey_obj.answersheet_set  # all answer sheets of this survey
	# only active response, which are all the students
	all_students = [
		((AnswerSheet.objects.filter(survey=survey_obj, student=answer_sheet.student).count()),
		 answer_sheet.student) for answer_sheet in
		all_responses.filter(active=True)]  # [(num of answer sheet, student obj)]

	num_students = len(all_students)
	num_responses = all_responses.count()

	context = {
		'num_students': num_students,
		'num_responses': num_responses,
		'all_responses': all_responses,
		'all_students': all_students,
		'survey_obj': survey_obj,

	}

	return render(request, 'survey/answer/student_list.html', context)


@require_http_methods(['GET'])
@login_required(login_url="/login")
def answer_sheet_list(request, survey_id, student_id):
	"""list all answer sheet of a student that response to this survey"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	student_obj = get_object_or_404(Student, pk=student_id)
	answer_sheet_set = AnswerSheet.objects.filter(survey=survey_obj, student=student_obj)
	num_answer_sheet = answer_sheet_set.count()
	context = {
		'answer_sheet_set': answer_sheet_set,
		'student_obj': student_obj,
		'survey_obj': survey_obj,
		'num_answer_sheet': num_answer_sheet
	}

	return render(request, 'survey/answer/answer_sheet_list.html', context)


@require_http_methods(['GET'])
@login_required(login_url="/login")
def answer_sheet_detail(request, survey_id, answer_sheet_id):
	"""detail answer sheet view"""
	current_instructor = request.user
	survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
	answer_sheet_obj = AnswerSheet(answer_sheet_id=answer_sheet_id, survey=survey_obj)
	question_answer_set = answer_sheet_obj.get_answers()  # list of (question,query set)
	context = {
		'question_answer_set': question_answer_set
	}
	return render(request, 'survey/answer/answer_sheet_detail.html', context)


# not required login
def survey_answer(request, survey_id):
	"""student answer the survey"""
	survey = get_object_or_404(Survey, survey_id=survey_id)

	if request.method == "POST":
		student_form = StudentCreationFrom(request.POST)
		if student_form.is_valid():
			student = student_form.save()
		else:
			raise Http404
		survey_answer_form = SurveyForm(request.POST, survey=survey, student=student)
		if survey_answer_form.is_valid():
			survey_answer_form.save()

	else:
		student_form = StudentCreationFrom()
		survey_answer_form = SurveyForm(None, survey=survey, student=None)

	context = {
		'student_form': student_form,
		'survey_answer_form': survey_answer_form,
		'survey': survey
	}
	return render(request, 'survey/answer/survey_answer.html', context)