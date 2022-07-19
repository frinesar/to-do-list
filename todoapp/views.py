from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import redirect, render
from .models import Task
from datetime import datetime

from random import choice

from .forms import CreateTaskForm, UpdateTaskForm, LoginForm


def index(request):
    return HttpResponse('Stub')


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    greetings = ['Hello there', "How it's doing", 'Good to see you']


    def get_context_data(self, *args, **kwargs):
        context = super(TasksListView, self).get_context_data(*args, **kwargs)
        context['greetings'] = choice(self.greetings)
        return context
    

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = UpdateTaskForm 
    success_url = reverse_lazy('tasks')

    def get_context_data(self, *args, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(*args, **kwargs)
        context['edit'] = True
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    


class TaskLoginView(LoginView):
    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = 'todoapp/task_login.html'   

    def get_success_url(self):
        return reverse_lazy('tasks')

