"""url for survey create/update/view detail"""

from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views_student,views_question,views_survey,views_option,views_upload,views


app_name = "survey"

urlpatterns = [
    # path('<slug:instance_slug>/create-update-survey/', views.create_update_survey, name='survey_create_update'),
    # survey
    path('<slug:instance_slug>/create-survey/', views_survey.create_survey, name='create_survey'),  # create survey
    path('<int:survey_id>/', views_survey.survey_index, name='survey_index'),  # list all questions and survey info

    # questions
    path('<int:survey_id>/questions/all/', views_question.question_list, name='question_list'),  # show all questions
    path('<int:survey_id>/questions/add/', views_question.add_question, name='add_question'),  # add question
    path('<int:survey_id>/questions/upload-csv/', views_upload.upload_questions_csv, name='upload_questions_csv'),
    # upload questions to a survey
    path('<int:survey_id>/question/<int:question_id>/', views_question.edit_question, name='edit_question'),  # edit question

    # options
    path('<int:survey_id>/question/<int:question_id>/options/add/', views_option.add_option, name='add_option'),
    path('question/<int:question_id>/options/delete/<int:pk>/delete', views_option.delete_option, name='delete_option'),
    path('<int:survey_id>/question/<int:question_id>/options/all/', views_option.option_list, name='option_list'),
    path('option_sort/<int:question_id>/', views_option.option_sort, name='option_sort'),

    # student answer
    path('<int:survey_id>/student-answer/', views.survey_answer, name='survey_answer'),
    path('<int:survey_id>/student-answer/upload', views_upload.upload_answers_csv, name='upload_answers_csv'),
    path('<int:survey_id>/students/all/', views_student.student_list, name='student_list'), # view all students answer this survey
    path('<int:survey_id>/student/<int:student_id>/all', views_student.answer_sheet_list, name='answer_sheet_list'), # list of a answer sheet of the student
    path('<int:survey_id>/answer-sheet/<int:answer_sheet_id>/', views_student.answer_sheet_detail, name='answer_sheet_detail'), # detail view of answer sheet


    path('thank-you/', TemplateView.as_view(template_name="survey/answer/thank_you.html"), name="thank-you")
]
