# Generated by Django 5.0.3 on 2024-05-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_trainer_nickname_alter_trainer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='001.png', null=True, upload_to=''),
        ),
    ]
