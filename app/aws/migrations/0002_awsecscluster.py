# Generated by Django 4.1.5 on 2023-01-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aws", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AWSECSCluster",
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
                ("cluster_name", models.CharField(max_length=30)),
            ],
        ),
    ]
