# Generated by Django 4.0.3 on 2022-04-20 16:03

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("postkon_webapp", "0008_alter_post_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="slug",
            field=django_extensions.db.fields.AutoSlugField(
                blank=True, editable=False, populate_from="user", unique=True
            ),
        ),
    ]
