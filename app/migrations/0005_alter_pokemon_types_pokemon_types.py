# Generated by Django 5.0.3 on 2024-05-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_pokemon_health_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon_types',
            name='pokemon_types',
            field=models.CharField(choices=[('fire', 'Fire'), ('fighting', 'Fighting'), ('flying', 'Flying'), ('grass', 'Grass'), ('ground', 'Ground'), ('water', 'Water')], max_length=50),
        ),
    ]
