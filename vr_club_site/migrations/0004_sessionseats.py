# Generated by Django 4.2.1 on 2023-07-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vr_club_site", "0003_bookingtime_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="SessionSeats",
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
                ("number", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
