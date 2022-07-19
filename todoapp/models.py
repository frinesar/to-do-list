from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True)
    title = models.CharField(max_length=25, verbose_name='Задание') 
    description = models.TextField(blank=True, verbose_name='Описание')
    time_stamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_finished = models.BooleanField(default=False, verbose_name='Выполнено')


    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'