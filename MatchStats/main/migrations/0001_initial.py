# Generated by Django 4.2 on 2023-05-01 18:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("name", models.CharField(max_length=128)),
                ("jersey_no", models.PositiveSmallIntegerField(null=True)),
                ("dob", models.DateField()),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("G", "Goalkeeper"),
                            ("D", "Defender"),
                            ("M", "Midfielder"),
                            ("F", "Forward"),
                        ],
                        max_length=1,
                    ),
                ),
                ("goals", models.PositiveSmallIntegerField(default=0)),
                ("assists", models.PositiveSmallIntegerField(default=0)),
                ("yellow_cards", models.PositiveSmallIntegerField(default=0)),
                ("red_cards", models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Stadium",
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
                ("name", models.CharField(max_length=128, unique=True)),
                ("address", models.CharField(max_length=512)),
                ("city", models.CharField(max_length=64)),
                ("capacity", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=128, unique=True)),
                ("code", models.CharField(max_length=3, unique=True)),
                ("goals_scored", models.PositiveSmallIntegerField()),
                ("goals_conceded", models.PositiveSmallIntegerField()),
                ("points", models.SmallIntegerField()),
                (
                    "stadium",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.stadium",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transfer",
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
                    "price",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.0)]
                    ),
                ),
                ("transfer_date", models.DateField()),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.player"
                    ),
                ),
                (
                    "team_from",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="team_from",
                        to="main.team",
                    ),
                ),
                (
                    "team_to",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="team_to",
                        to="main.team",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.team",
            ),
        ),
        migrations.CreateModel(
            name="Match",
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
                ("score_1", models.PositiveSmallIntegerField(default=0)),
                ("score_2", models.PositiveSmallIntegerField(default=0)),
                ("shots_1", models.PositiveSmallIntegerField(default=0)),
                ("shots_2", models.PositiveSmallIntegerField(default=0)),
                ("offsides_1", models.PositiveSmallIntegerField(default=0)),
                ("offsides_2", models.PositiveSmallIntegerField(default=0)),
                ("corners_1", models.PositiveSmallIntegerField(default=0)),
                ("corners_2", models.PositiveSmallIntegerField(default=0)),
                ("match_time", models.DateTimeField()),
                ("completed", models.BooleanField(default=False)),
                ("viewer_count", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "stadium",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.stadium",
                    ),
                ),
                (
                    "team_1",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="team_1",
                        to="main.team",
                    ),
                ),
                (
                    "team_2",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="team_2",
                        to="main.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Goal",
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
                ("match_time", models.DateTimeField()),
                (
                    "assist",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assist_set",
                        to="main.player",
                    ),
                ),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.match"
                    ),
                ),
                (
                    "scorer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="goal_set",
                        to="main.player",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.team",
                    ),
                ),
            ],
        ),
    ]
