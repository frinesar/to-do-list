from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'time_stamp', 'is_finished')
    list_display_links = ('title',)
    search_fields = ('title', 'description')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Task, TaskAdmin)
admin.site.register(User, AuthorAdmin)
