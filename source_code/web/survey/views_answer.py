from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, Http404, get_object_or_404
from .forms import LockSurveyForm, StudentCreationFrom, SurveyForm
from .models import Survey


@login_required(login_url="/login")
def send_survey(request, survey_id=None):
	"""lock the survey and generate answer link"""
	current_user = request.user
	survey_obj = get_object_or_404(Survey,
	                               survey_id=survey_id)
	if current_user != survey_obj.instance.instructor:
		redirect('/login')

	if request.method == "PUT":
		lock_survey_form = LockSurveyForm(request.PUT, None)
		context = {
			"survey": survey_obj
		}
		if lock_survey_form.is_valid():
			survey_obj.modify = True
			survey_obj.save()
		return render(request, 'survey/answer/answer_url_link.html', context)


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
