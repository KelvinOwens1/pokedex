# Generated by Django 5.0.3 on 2024-05-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_trainer_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(default='Full Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='nickname',
            field=models.CharField(default='Name', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar_6388000.png', null=True, upload_to=''),
        ),
    ]