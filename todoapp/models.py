from tabnanny import verbose
from turtle import mode
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=25, verbose_name='Автор')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


    def __str__(self) -> str:
        return self.name


class Task(models.Model):

    author = models.ForeignKey('Author', null=True, on_delete=models.PROTECT, verbose_name='Автор')
    title = models.CharField(max_length=25, verbose_name='Задание')
    text = models.TextField(blank=True, verbose_name='Текст')
    time_stamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_finished = models.BooleanField(default=False, verbose_name='Выполнено')


    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'