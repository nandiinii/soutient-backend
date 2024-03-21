# Generated by Django 5.0.3 on 2024-03-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Election",
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
                ("no_of_votes", models.IntegerField()),
                ("name_of_campaign", models.CharField(max_length=30)),
                ("start_date", models.DateTimeField()),
                ("creator", models.CharField(max_length=400)),
                ("end_date", models.DateTimeField()),
                ("is_open", models.BooleanField(default=False)),
                ("voted_users_json", models.TextField(default="[]")),
            ],
        ),
    ]
