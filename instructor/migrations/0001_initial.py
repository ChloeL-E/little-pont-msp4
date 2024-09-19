# Generated by Django 3.2.25 on 2024-08-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Intructor",
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
                ("instructor_name", models.CharField(max_length=50)),
                ("bio_description", models.TextField()),
                ("experience", models.TextField()),
                ("speciality_age_group", models.CharField(max_length=50)),
            ],
        ),
    ]
