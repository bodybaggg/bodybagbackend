# Generated by Django 4.2.9 on 2024-02-04 10:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_user_notification_enabled"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="notification_enabled",
        ),
    ]
