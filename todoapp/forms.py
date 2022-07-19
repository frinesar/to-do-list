from django.contrib.auth.forms import AuthenticationForm
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


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'username'}
        )

        self.fields['password'].widget.attrs.update(
            {'class': 'password'}
        )   