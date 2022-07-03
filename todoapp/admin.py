from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'time_stamp', 'is_finished')
    list_display_links = ('title',)
    search_fields = ('title', 'text')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Author, AuthorAdmin)
