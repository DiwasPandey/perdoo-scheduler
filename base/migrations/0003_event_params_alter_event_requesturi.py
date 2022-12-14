# Generated by Django 4.1 on 2022-09-06 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_event_requestmethod"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="params",
            field=models.JSONField(default="", verbose_name="params"),
        ),
        migrations.AlterField(
            model_name="event",
            name="requestURI",
            field=models.URLField(max_length=500),
        ),
    ]
