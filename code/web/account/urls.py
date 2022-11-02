"""urls for register/login/logout"""
from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.register, name='register'),
]
