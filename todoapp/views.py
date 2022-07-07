from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render
from .models import Task
from datetime import datetime

from .forms import CreateTaskForm, UpdateTaskForm


def index(request):
    return HttpResponse('Stub')


class TasksListView(ListView):
    model = Task
    context_object_name = 'tasks'
    # queryset = Task.objects.filter(user_id__name='Лешик')


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    success_url = reverse_lazy('tasks')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = UpdateTaskForm 
    success_url = reverse_lazy('tasks')

    def get_context_data(self, *args, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(*args, **kwargs)
        context['edit'] = True
        return context


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')




