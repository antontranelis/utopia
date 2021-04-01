# Generated by Django 3.1.7 on 2021-03-27 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0021_auto_20210315_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(default='#000', max_length=25),
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, to='map.Tag'),
        ),
        migrations.AlterField(
            model_name='place',
            name='tags',
            field=models.ManyToManyField(blank=True, to='map.Tag'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]