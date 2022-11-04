"""url for survey create/update/view detail"""

from django.urls import path, include
from . import views

app_name = "survey"

urlpatterns = [
	path('<slug:instance_slug>/create/', views.create_survey, name='create'),
	path('<slug:instance_slug>/<int:survey_id>/edit/', views.update_survey, name='update'),
	path('<slug:instance_slug>/<int:survey_id>', views.detail_survey, name='detail'),
]
