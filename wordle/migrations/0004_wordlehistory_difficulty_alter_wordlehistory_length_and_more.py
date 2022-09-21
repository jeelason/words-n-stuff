# Generated by Django 4.1.1 on 2022-09-21 06:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wordle", "0003_wordlehistory_guesses_needed"),
    ]

    operations = [
        migrations.AddField(
            model_name="wordlehistory",
            name="difficulty",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="wordlehistory",
            name="length",
            field=models.PositiveSmallIntegerField(
                default=5,
                validators=[
                    django.core.validators.MaxValueValidator(9),
                    django.core.validators.MinValueValidator(4),
                ],
                verbose_name="Word length",
            ),
        ),
        migrations.AlterField(
            model_name="wordlehistory",
            name="tries",
            field=models.PositiveSmallIntegerField(
                default=6,
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(3),
                ],
                verbose_name="Guesses allowed",
            ),
        ),
    ]