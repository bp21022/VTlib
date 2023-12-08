# Generated by Django 4.1 on 2023-11-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0005_link_post_created_at_alter_post_image_post_links"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="links",
        ),
        migrations.DeleteModel(
            name="Link",
        ),
        migrations.AddField(
            model_name="post",
            name="links",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
