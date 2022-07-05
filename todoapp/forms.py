from django.forms import ModelForm

from .models import *

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'text')