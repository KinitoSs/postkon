# Generated by Django 4.2.1 on 2023-05-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("postkon_webapp", "0015_moderator"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_banned",
            field=models.BooleanField(default=False),
        ),
    ]
