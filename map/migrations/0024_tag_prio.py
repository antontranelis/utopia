# Generated by Django 3.1.7 on 2021-03-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0023_auto_20210327_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='prio',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
