"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = "iGroup"

urlpatterns = [

	path('home/', views.index, name='home'),  # instance home page, list all instances
	path('create/', views.create_instance, name='create'),
	path('<slug:slug>/delete/', views.delete, name='delete'),
	path('<slug:slug>/', views.detail_instance, name='detail'),

	path('<slug:slug>/config/create/', views.config_instance, name="config"),  # configuration for running the instance
	path('<slug:slug>/config/all/', views.list_config, name="list_config"),
	path('<slug:slug>/config/<int:config_id>/', views.detail_config, name="detail_config"),
	path('<slug:slug>/result/<int:config_id>/', views.detail_result, name="detail_result"),

]
