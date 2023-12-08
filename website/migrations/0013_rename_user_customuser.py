# Generated by Django 4.1 on 2023-12-01 13:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("account", "0005_emailaddress_idx_upper_email"),
        ("socialaccount", "0006_alter_socialaccount_extra_data"),
        ("website", "0012_rename_customuser_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="CustomUser",
        ),
    ]
