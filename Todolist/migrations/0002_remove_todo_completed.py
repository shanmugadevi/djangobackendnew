# Generated by Django 3.1.6 on 2021-02-14 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
    ]
