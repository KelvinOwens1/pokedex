# Generated by Django 5.0.3 on 2024-05-20 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_trainer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='health_points',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='is_caught',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='level',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='owner',
        ),
    ]
