# Generated by Django 5.0.3 on 2024-03-22 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_username_userblocked'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserBlocked',
            new_name='BlockedUser',
        ),
    ]
