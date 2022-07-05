from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render
from .models import Task
from datetime import datetime

from .forms import AddTaskForm



def get_task_by_id(request, task_id):
    task = Task.objects.get(pk=task_id)
    form = AddTaskForm({'title': task.title,
                        'text': task.text,
                        'pk': task.pk,
                        'author': 'ВАЛЕРА'})
    context = {'form': form}
    return render(request, 'todoapp/task.html', context)



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


class TasksListView(ListView):
    model = Task
    template_name = 'todoapp/index.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    form_class = AddTaskForm
    success_url = reverse_lazy('index')
    template_name = 'todoapp/index.html'


class TaskDetailView(DetailView):
    model = Task


# class TaskDeleteView(DetailView):
#     model = Task
#     context_object_name = 'task'
#     success_url = reverse_lazy('index')

#     def get(self, request, *args, **kwargs):
#         return self.task(request, *args, **kwargs)
        



class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'text']
    success_url = reverse_lazy('index')







