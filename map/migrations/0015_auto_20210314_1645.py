# Generated by Django 3.1.7 on 2021-03-14 16:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0014_auto_20210314_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lat',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='lon',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='share_status',
            field=models.SmallIntegerField(choices=[(1, 'everyone can see'), (2, 'anyone with link'), (3, 'only specific users')], default=1, verbose_name='share status'),
        ),
        migrations.AddField(
            model_name='profile',
            name='share_users',
            field=models.ManyToManyField(blank=True, related_name='shared_positions', to=settings.AUTH_USER_MODEL, verbose_name='share with'),
        ),
        migrations.DeleteModel(
            name='UserPosition',
        ),
    ]
