# Generated by Django 3.1.7 on 2021-03-15 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0019_auto_20210315_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
