"""url for survey create/update/view detail"""

from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name = "survey"

urlpatterns = [
	path('<slug:instance_slug>/create-update-survey/', views.create_update_survey, name='survey_create_update'),
	path('question/<int:question_id>/create_update_option/', views.create_update_options, name='options_create_update'),
	path('<slug:instance_slug>/survey-review/', views.review, name='review'),
	path('<slug:instance_slug>/survey-lock/', views.survey_lock, name='lock'),
	path('<slug:instance_slug>/survey-response-link/', views.survey_response, name='response'),
	path('<int:survey_id>/student-answer/', views.survey_answer, name='survey_answer'),
	path('thank-you/', TemplateView.as_view(template_name="survey/answer/thank_you.html"), name="thank-you")
]
