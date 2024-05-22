# Generated by Django 5.0.3 on 2024-05-19 01:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pokemon_types",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pokemon_types",
                    models.CharField(
                        choices=[
                            ("fire", "Fire"),
                            ("fighting", "Fighting"),
                            ("flying", "Flying0"),
                            ("grass", "Grass"),
                            ("ground", "Ground"),
                            ("water", "Water"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=50, null=True)),
                ("name", models.CharField(max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("num", models.CharField(max_length=4)),
                ("name", models.CharField(max_length=50)),
                ("level", models.PositiveIntegerField(default=1, null=True)),
                ("health_points", models.PositiveIntegerField(null=True)),
                ("is_caught", models.BooleanField(default=False, null=True)),
                ("description", models.TextField(null=True)),
                ("evolutions", models.TextField(null=True)),
                (
                    "owner",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.player",
                    ),
                ),
                (
                    "pokemon_types",
                    models.ManyToManyField(
                        null=True,
                        related_name="type",
                        related_query_name="types",
                        to="app.pokemon_types",
                    ),
                ),
            ],
        ),
    ]
