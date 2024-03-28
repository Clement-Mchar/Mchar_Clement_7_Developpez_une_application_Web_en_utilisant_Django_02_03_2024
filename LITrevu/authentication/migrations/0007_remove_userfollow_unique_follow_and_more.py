# Generated by Django 5.0.3 on 2024-03-27 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_remove_userfollow_unique_follow_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="userfollow",
            name="unique_follow",
        ),
        migrations.AlterField(
            model_name="userfollow",
            name="followed_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="followed_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="userfollow",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddConstraint(
            model_name="userfollow",
            constraint=models.UniqueConstraint(
                fields=("followed_user", "user"), name="unique_follow"
            ),
        ),
    ]
