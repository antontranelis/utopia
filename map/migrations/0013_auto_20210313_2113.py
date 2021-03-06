# Generated by Django 3.1.7 on 2021-03-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_auto_20210313_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='map.Tag'),
        ),
        migrations.AddField(
            model_name='place',
            name='tags',
            field=models.ManyToManyField(to='map.Tag'),
        ),
        migrations.AddField(
            model_name='userposition',
            name='tags',
            field=models.ManyToManyField(to='map.Tag'),
        ),
    ]
