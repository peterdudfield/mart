# Generated by Django 2.1 on 2019-01-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("art", "0004_auto_20180916_1751"),
    ]

    operations = [
        migrations.AddField(
            model_name="art",
            name="shopurl",
            field=models.CharField(
                default="https://www.etsy.com/uk/shop/MathematicalArtShop", max_length=250
            ),
        ),
    ]
