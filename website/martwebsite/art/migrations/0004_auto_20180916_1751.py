# Generated by Django 2.1 on 2018-09-16 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("art", "0003_art_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="art",
            old_name="url",
            new_name="file",
        ),
    ]
