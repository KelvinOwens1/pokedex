# Generated by Django 5.0.3 on 2024-05-22 23:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0020_remove_pokemon_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Pokemon_types",
            new_name="Pokemon_type",
        ),
        migrations.RenameField(
            model_name="pokemon",
            old_name="pokemon_types",
            new_name="pokemon_type",
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="pokemon_pic",
            field=models.ImageField(
                blank=True, default="pokeball.png", null=True, upload_to=""
            ),
        ),
    ]
