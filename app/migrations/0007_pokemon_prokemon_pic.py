# Generated by Django 5.0.3 on 2024-05-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_pokemon_types_pokemon_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='prokemon_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
