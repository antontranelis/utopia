# Generated by Django 3.1.7 on 2021-04-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0025_profile_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(blank=True, to='map.Tag'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
