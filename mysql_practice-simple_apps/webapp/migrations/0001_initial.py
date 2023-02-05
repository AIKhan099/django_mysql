# Generated by Django 4.1.3 on 2022-11-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                ("course1", models.CharField(max_length=255)),
                ("subject1", models.CharField(max_length=255)),
                ("ratting1", models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]