# Generated by Django 4.2.5 on 2024-03-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ToekomstPiano", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userregistration",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userregistration",
            name="password",
            field=models.CharField(max_length=255),
        ),
    ]
