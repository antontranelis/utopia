# Generated by Django 3.1.7 on 2021-03-13 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20210313_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userposition',
            name='text',
        ),
        migrations.RemoveField(
            model_name='userposition',
            name='title',
        ),
    ]
