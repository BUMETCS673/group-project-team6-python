from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import InstructorChangeForm, InstructorCreationForm
from .models import Instructor, Student
from survey.models import Survey, AnswerSheet


class InstructorAdmin(UserAdmin):
    """instruction admin"""
    add_form = InstructorCreationForm
    form = InstructorChangeForm
    model = InstructorCreationForm
    list_display = ["email", "username", "first_name", "last_name", ]


admin.site.register(Instructor, InstructorAdmin)


class AnswerSheetInline(admin.TabularInline):
    model = AnswerSheet
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    inlines = [AnswerSheetInline, ]
