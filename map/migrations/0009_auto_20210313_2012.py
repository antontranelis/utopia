# Generated by Django 3.1.7 on 2021-03-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20210313_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='edit_status',
            field=models.SmallIntegerField(choices=[(1, 'Everyone can edit'), (2, 'Editors can edit'), (3, 'Just creator can edit')], default=3, verbose_name='edit status'),
        ),
        migrations.AlterField(
            model_name='place',
            name='edit_status',
            field=models.SmallIntegerField(choices=[(1, 'Everyone can edit'), (2, 'Editors can edit'), (3, 'Just creator can edit')], default=3, verbose_name='edit status'),
        ),
    ]
