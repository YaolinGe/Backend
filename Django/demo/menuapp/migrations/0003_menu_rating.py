# Generated by Django 4.2.8 on 2024-04-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menuapp", "0002_rename_name_menu_menu_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="rating",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
