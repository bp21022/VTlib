# Generated by Django 4.1 on 2023-12-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0015_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="account_image",
            field=models.ImageField(
                default="default_image.png", null=True, upload_to="img/"
            ),
        ),
    ]