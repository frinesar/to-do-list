from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'time_stamp', 'is_finished')
    list_display_links = ('title',)
    search_fields = ('title', 'description')



admin.site.register(Task, TaskAdmin)
