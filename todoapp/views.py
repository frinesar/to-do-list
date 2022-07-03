import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from datetime import datetime


def index(request):
    Task.objects.create(title='Стоматолог', text='Прием у стоматолога на 16:00')


    records = ''
    # if tasks := Task.objects.filter(time_stamp__lt=datetime(2022, 6, 30, 16, 7)):
    if tasks := Task.objects.all():
        for task in tasks:
            
            records += str(f'{task.pk} \t {task.title} \t {task.text} \t {task.time_stamp} \t {task.is_finished}\n')
            

        return HttpResponse(records, content_type='text/plain; charset=utf-8')

    else:
        return HttpResponse('No records')


def get_by_author_name(request, author_id):
    tasks = Task.objects.filter(author=author_id)
    context = {'tasks': tasks}
    return render(request, 'todoapp/index.html', context)