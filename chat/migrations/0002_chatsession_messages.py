# Generated by Django 4.2 on 2024-04-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatsession",
            name="messages",
            field=models.ManyToManyField(blank=True, to="chat.message"),
        ),
    ]
