# Generated by Django 4.1.3 on 2023-01-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("digital_App", "0002_role_rename_user_chairman_visitor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="Role_Type",
            field=models.CharField(
                blank=True,
                choices=[("M", "member"), ("C", "chairman")],
                default="",
                max_length=5,
            ),
        ),
    ]
