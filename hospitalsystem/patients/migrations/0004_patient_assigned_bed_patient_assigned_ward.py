# Generated by Django 4.1.3 on 2023-02-18 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0003_remove_doctor_number_of_patients"),
        ("patients", "0003_patient_assigned_doctor"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="assigned_bed",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="patient",
            name="assigned_ward",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="hospital.ward",
            ),
        ),
    ]
