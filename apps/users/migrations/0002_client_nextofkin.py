# Generated by Django 4.2 on 2024-08-22 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone_number", models.CharField(max_length=255)),
                ("id_number", models.CharField(max_length=255, null=True)),
                ("kra_pin", models.CharField(max_length=255, null=True)),
                ("gender", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255, null=True)),
                ("city", models.CharField(max_length=255, null=True)),
                ("country", models.CharField(max_length=255, null=True)),
                ("id_copy", models.FileField(null=True, upload_to="client_ids/")),
                (
                    "kra_certificate",
                    models.FileField(null=True, upload_to="kra_cerificates/"),
                ),
                ("photo", models.ImageField(null=True, upload_to="client_photos/")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NextOfKin",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("relation", models.CharField(max_length=255)),
                ("gender", models.CharField(max_length=255, null=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nextofkins",
                        to="users.client",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]