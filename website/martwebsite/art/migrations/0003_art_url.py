# Generated by Django 2.1 on 2018-09-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("art", "0002_art_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="art",
            name="url",
            field=models.FileField(default="default", upload_to=""),
            preserve_default=False,
        ),
    ]
