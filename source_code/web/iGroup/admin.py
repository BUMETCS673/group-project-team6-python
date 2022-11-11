from django.contrib import admin
from .models import Instance, ConfigInstance, ResultInstance
from django.contrib import admin


# Register your models here.

class InstanceAdmin(admin.ModelAdmin):
	list_display = ('instance_id', 'instance_name', 'slug')


admin.site.register(Instance)
admin.site.register(ConfigInstance)

admin.site.register(ResultInstance)
