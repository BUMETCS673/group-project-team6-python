from django.contrib import admin
from .models import Survey, AnswerSheet, Question, Option, ChoiceMultiple, ChoiceSingle

# Register your models here.

# admin.site.register(Answer)
admin.site.register(Option)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('survey_id', 'survey_name')


class OptionAdmin(admin.TabularInline):
    model = Option


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ('question_index', 'survey',)
    inlines = [OptionAdmin, ]


class ChoiceMultipleAdmin(admin.TabularInline):
    model = ChoiceMultiple


class ChoiceSingleAdmin(admin.TabularInline):
    model = ChoiceSingle


@admin.register(AnswerSheet)
class AnswerSheet(admin.ModelAdmin):
    list_display = ('student', 'survey',)
    inlines = [ChoiceMultipleAdmin, ChoiceSingleAdmin]
