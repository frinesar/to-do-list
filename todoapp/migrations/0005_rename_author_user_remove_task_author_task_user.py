# Generated by Django 4.0.5 on 2022-07-07 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_remove_task_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapp.user', verbose_name='Автор'),
        ),
    ]
