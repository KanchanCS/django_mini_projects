# Generated by Django 4.1.7 on 2023-03-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app", "0002_delete_bookmarks"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bookmarks",
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
                ("title", models.CharField(max_length=100)),
                ("url", models.URLField(blank=True)),
                ("createdate", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
