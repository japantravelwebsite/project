# Generated by Django 4.1.7 on 2023-05-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_picture_db_etc4_remove_picture_db_etc5_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="image_db",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("content", models.CharField(max_length=100)),
            ],
        ),
    ]
