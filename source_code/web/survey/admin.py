from django.contrib import admin
from .models import Survey, AnswerSheet, Question, Answer, Option

# Register your models here.

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(AnswerSheet)
admin.site.register(Answer)
admin.site.register(Option)
