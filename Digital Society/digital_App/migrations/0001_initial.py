# Generated by Django 4.1.3 on 2022-12-09 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Events",
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
                ("AddEvent", models.CharField(blank=True, default="", max_length=50)),
                ("Date", models.DateField()),
            ],
            options={"db_table": "Events",},
        ),
        migrations.CreateModel(
            name="Notices",
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
                (
                    "AddNotices",
                    models.TextField(blank=True, default="", max_length=150),
                ),
                ("Date", models.DateField()),
            ],
            options={"db_table": "Notices",},
        ),
        migrations.CreateModel(
            name="Transactions",
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
            ],
            options={"db_table": "Transactions",},
        ),
        migrations.CreateModel(
            name="User",
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
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=12)),
            ],
            options={"db_table": "User",},
        ),
        migrations.CreateModel(
            name="Watchmans",
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
                ("FullName", models.CharField(blank=True, default="", max_length=20)),
                ("Mobile", models.CharField(blank=True, default="", max_length=10)),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="digital_App.user",
                    ),
                ),
            ],
            options={"db_table": "Watchmans",},
        ),
        migrations.CreateModel(
            name="Visitors",
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
                ("FullName", models.CharField(blank=True, default="", max_length=20)),
                ("Mobile", models.CharField(blank=True, default="", max_length=10)),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="digital_App.user",
                    ),
                ),
            ],
            options={"db_table": "Visitors",},
        ),
        migrations.CreateModel(
            name="Notices_views",
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
                (
                    "Notices",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="digital_App.notices",
                    ),
                ),
            ],
            options={"db_table": "Notices_views",},
        ),
        migrations.CreateModel(
            name="Members",
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
                ("FullName", models.CharField(blank=True, default="", max_length=15)),
                ("Mobile", models.CharField(blank=True, default="", max_length=10)),
                (
                    "Gender",
                    models.CharField(
                        blank=True,
                        choices=[("m", "Male"), ("f", "Female")],
                        default="",
                        max_length=6,
                    ),
                ),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="digital_App.user",
                    ),
                ),
            ],
            options={"db_table": "Members",},
        ),
        migrations.CreateModel(
            name="Chairmans",
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
                ("FullName", models.CharField(blank=True, default="", max_length=15)),
                ("Mobile", models.CharField(blank=True, default="", max_length=10)),
                (
                    "Gender",
                    models.CharField(
                        blank=True,
                        choices=[("m", "Male"), ("f", "Female")],
                        default="",
                        max_length=6,
                    ),
                ),
                (
                    "User",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="digital_App.user",
                    ),
                ),
            ],
            options={"db_table": "Chairmans",},
        ),
    ]
