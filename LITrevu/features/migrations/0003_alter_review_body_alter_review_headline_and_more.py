# Generated by Django 5.0.3 on 2024-03-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("features", "0002_delete_userfollow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="body",
            field=models.TextField(
                blank=True, verbose_name="Corps du message"
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="headline",
            field=models.CharField(max_length=128, verbose_name="Titre"),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.TextField(
                blank=True, max_length=2048, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="title",
            field=models.CharField(max_length=128, verbose_name="Titre"),
        ),
    ]
