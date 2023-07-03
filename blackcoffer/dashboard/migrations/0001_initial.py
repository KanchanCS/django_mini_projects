# Generated by Django 4.1.7 on 2023-02-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IndustrySummary",
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
                ("topic", models.CharField(max_length=75)),
                ("region", models.CharField(blank=True, max_length=75)),
                ("sector", models.CharField(blank=True, max_length=75)),
                ("country", models.CharField(blank=True, max_length=100)),
                ("pestle", models.CharField(blank=True, max_length=100)),
                ("sources", models.CharField(blank=True, max_length=100)),
                ("impact", models.CharField(blank=True, max_length=75)),
                ("insight", models.CharField(blank=True, max_length=100)),
                ("title", models.TextField(default="")),
                ("url", models.URLField(blank=True)),
                ("likelihood", models.IntegerField(default=0, null=True)),
                ("relevance", models.IntegerField(default=0, null=True)),
                ("intensity", models.IntegerField(default=0, null=True)),
                ("start_year", models.DateField(null=True)),
                ("end_year", models.DateField(null=True)),
                ("add_date", models.DateTimeField(null=True)),
                ("publish_date", models.DateTimeField(null=True)),
            ],
        ),
    ]
