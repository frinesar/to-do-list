from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .models import Task
from datetime import datetime

from .forms import AddTaskForm


def index(request):

    if tasks := Task.objects.all():
        context = {'tasks': tasks, 'title': 'ToDoList'}
        return render(request, 'todoapp/index.html', context)
    else:
        return HttpResponse('No records')


def get_by_author_name(request, author_id):
    tasks = Task.objects.filter(author=author_id)
    context = {'tasks': tasks}
    return render(request, 'todoapp/index.html', context)



def test(request):
    return render(request, 'todoapp/index.html')


def add_new_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                print('Unable to add new task')

    else:
        form = AddTaskForm()
        context = {'form': form}
        return render(request, 'todoapp/index.html', context)


class TaskCreateView(CreateView):

    form_class = AddTaskForm
    success_url = reverse_lazy('index')
    template_name = 'todoapp/index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
