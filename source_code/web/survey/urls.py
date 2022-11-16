"""url for survey create/update/view detail"""

from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name = "survey"

urlpatterns = [
    # path('<slug:instance_slug>/create-update-survey/', views.create_update_survey, name='survey_create_update'),
    path('<slug:instance_slug>/create-survey/', views.create_survey, name='create_survey'),  # create survey
    path('<int:survey_id>/', views.survey_index, name='survey_index'),  # list all questions and survey info
    path('<int:survey_id>/questions/all/', views.question_list, name='question_list'),
    path('<int:survey_id>/questions/add/', views.add_question, name='add_question'),  # add question
    path('<int:survey_id>/question/<int:question_id>/', views.edit_question, name='edit_question'),  # edit question
    path('<int:survey_id>/question/<int:question_id>/options/add/', views.add_option, name='add_option'),
    path('question/<int:question_id>/options/delete/<int:pk>/', views.delete_option, name='delete_option'),
    path('<int:survey_id>/question/<int:question_id>/options/all/', views.option_list, name='option_list'),
    path('option_sort/<int:question_id>/',views.option_sort, name='option_sort'),
    # path('question/<int:question_id>/create_update_option/', views.create_update_options, name='options_create_update'),
    path('<int:survey_id>/student-answer/', views.survey_answer, name='survey_answer'),

    path('thank-you/', TemplateView.as_view(template_name="survey/answer/thank_you.html"), name="thank-you")
]
