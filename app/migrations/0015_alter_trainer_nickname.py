# Generated by Django 5.0.3 on 2024-05-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_trainer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='nickname',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]