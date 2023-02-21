# Generated by Django 4.1.3 on 2023-02-18 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                ("phone_number", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("med_history", models.TextField()),
                ("blood_type", models.CharField(max_length=50)),
            ],
        ),
    ]