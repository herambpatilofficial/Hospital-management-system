# Generated by Django 4.1.3 on 2023-02-18 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0002_remove_doctor_patients"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="number_of_patients",
        ),
    ]