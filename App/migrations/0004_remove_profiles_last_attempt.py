# Generated by Django 4.1.7 on 2023-11-12 19:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0003_alter_jobs_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profiles",
            name="last_attempt",
        ),
    ]
