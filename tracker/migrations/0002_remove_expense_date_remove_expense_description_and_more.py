# Generated by Django 5.1.4 on 2025-01-20 11:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="expense",
            name="date",
        ),
        migrations.RemoveField(
            model_name="expense",
            name="description",
        ),
        migrations.AddField(
            model_name="expense",
            name="date_added",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
