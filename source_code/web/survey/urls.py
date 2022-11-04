"""url for survey create/update/view detail"""

from django.urls import path, include
from . import views

app_name = "survey"

urlpatterns = [
	path('<slug:instance_slug>/create-update-survey/', views.create_update_survey, name='survey_create_update'),
	path('survey/question/<int:question_id>/create_update_option/', views.create_update_options, name='options_create_update'),
	path('<slug:instance_slug>/survey-review/', views.review, name='review'),
	path('<slug:instance_slug>/survey-lock/', views.survey_lock, name='lock'),
	path('<slug:instance_slug>/survey-response-link/', views.survey_response, name='response')
]
