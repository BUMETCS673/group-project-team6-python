from django.contrib import admin
from .models import Instance, ConfigInstance, ResultTeam, ResultQuestionScore, StudentTeam
from django.contrib import admin
from nested_admin import NestedTabularInline, NestedModelAdmin


# Register your models here.

class InstanceAdmin(admin.ModelAdmin):
	list_display = ('instance_id', 'instance_name', 'slug')



class StudentTeamInline(NestedTabularInline):
	model = StudentTeam
	extra = 0

class ResultTeamInline(NestedTabularInline):
	model = ResultTeam
	extra = 0
	inlines = [StudentTeamInline]


@admin.register(ConfigInstance)
class ConfigInstanceAdmin(NestedModelAdmin):
	inlines = [ResultTeamInline]


admin.site.register(Instance)
