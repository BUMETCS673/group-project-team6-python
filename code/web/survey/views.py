from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate


@login_required(login_url="/login")
def create_survey(request):
	"""create a new survey from form"""
	return


@login_required(login_url="/login")
def update_survey(request, id=None):
	"""update a survey"""

	return


@login_required(login_url="/login")
def delete_survey(request, id=None):
	"""update a survey"""
	return
