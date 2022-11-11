from django.contrib import admin
from .models import Survey, AnswerSheet, Question, Option, ChoiceMultiple, ChoiceSingle

# Register your models here.

admin.site.register(Question)
admin.site.register(AnswerSheet)
# admin.site.register(Answer)
admin.site.register(Option)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
	list_display = ('survey_id', 'survey_name')


@admin.register(ChoiceMultiple)
class ChoiceMultiple(admin.ModelAdmin):
	list_display = (
		'rank',
		'option',
	)


@admin.register(ChoiceSingle)
class ChoiceSingle(admin.ModelAdmin):
	list_display = ('option',)
