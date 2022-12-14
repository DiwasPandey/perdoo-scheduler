# Generated by Django 4.1 on 2022-09-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="requestMethod",
            field=models.CharField(
                choices=[
                    ("POST", "POST"),
                    ("GET", "GET"),
                    ("PUT", "PUT"),
                    ("DELETE", "DELETE"),
                ],
                default="POST",
                max_length=6,
            ),
        ),
    ]
