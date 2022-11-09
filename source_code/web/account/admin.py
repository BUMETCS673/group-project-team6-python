from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import InstructorChangeForm, InstructorCreationForm
from .models import Instructor,Student


class InstructorAdmin(UserAdmin):
	"""instruction admin"""
	add_form = InstructorCreationForm
	form = InstructorChangeForm
	model = InstructorCreationForm
	list_display = ["email", "username", "first_name", "last_name", ]


admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student)