from django.forms import *
from .models import *

class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')
        widgets = {
            'title': TextInput(attrs={'class': 'title'}),
            'description': Textarea(attrs={'class': 'description'}),
        }



class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'is_finished')
        widgets = {
            'title': TextInput(attrs={'class': 'title'}),
            'description': Textarea(attrs={'class': 'description'}),
        }