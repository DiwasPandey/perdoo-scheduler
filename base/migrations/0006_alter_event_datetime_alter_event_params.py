# Generated by Django 4.1 on 2022-09-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_event_params"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="datetime",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="params",
            field=models.JSONField(
                blank=True, default=dict, null=True, verbose_name="params"
            ),
        ),
    ]
