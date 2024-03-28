# Generated by Django 5.0.3 on 2024-03-27 16:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("features", "0003_alter_review_body_alter_review_headline_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.BooleanField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
    ]
