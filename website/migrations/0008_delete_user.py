# Generated by Django 4.1 on 2023-11-30 09:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0007_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
