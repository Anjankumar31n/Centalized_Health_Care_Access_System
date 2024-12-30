# Generated by Django 4.2 on 2024-03-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("healthScore", "0004_user_groups_user_is_superuser_user_last_login_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.TextField(blank=True, default="", max_length=255),
        ),
    ]
