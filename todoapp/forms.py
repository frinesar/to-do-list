from django.forms import ModelForm

from .models import *

class TaskFrom(ModelForm):
    class Meta:
        model = Task
        fields = ('author', 'title', 'text')