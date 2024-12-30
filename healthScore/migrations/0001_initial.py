# Generated by Django 4.2.10 on 2024-02-21 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="appointment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("properties", models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="hospital",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("address", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("password", models.TextField()),
                ("contactInfo", models.TextField(max_length=10)),
                ("website", models.TextField(default="")),
                (
                    "status",
                    models.TextField(
                        choices=[
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                            ("pending", "Pending"),
                        ],
                        default="pending",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="user",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254)),
                ("name", models.TextField()),
                ("password", models.TextField()),
                ("userName", models.CharField(max_length=50, unique=True)),
                ("dob", models.DateField()),
                ("contactInfo", models.TextField(default="", max_length=10)),
                ("proofOfIdentity", models.TextField()),
                ("address", models.TextField()),
                ("securityQues", models.TextField(default="")),
                ("securityAns", models.TextField(default="")),
                ("gender", models.TextField(default="")),
                ("profilePic", models.TextField(null=True)),
                ("bloodGroup", models.TextField()),
                ("requests", models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="hospitalStaff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("admin", models.BooleanField(default=False)),
                ("name", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("password", models.TextField()),
                ("specialization", models.TextField(default="")),
                ("contactInfo", models.TextField(default="", max_length=10)),
                ("securityQues", models.TextField(default="")),
                ("securityAns", models.TextField(default="")),
                (
                    "hospitalID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthScore.hospital",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="healthRecord",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("doctorID", models.TextField()),
                ("hospitalID", models.TextField()),
                (
                    "status",
                    models.TextField(
                        choices=[
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                            ("pending", "Pending"),
                        ],
                        default="pending",
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now_add=True)),
                ("healthDocuments", models.JSONField(null=True)),
                (
                    "appointmentId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthScore.appointment",
                    ),
                ),
                (
                    "userID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthScore.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="communityInteraction",
            fields=[
                ("postID", models.AutoField(primary_key=True, serialize=False)),
                ("postTitle", models.TextField()),
                ("postDescription", models.TextField(default="")),
                ("postTimeStamp", models.DateTimeField(auto_now_add=True)),
                ("upvote", models.IntegerField(default=0)),
                ("downvote", models.IntegerField(default=0)),
                ("tags", models.TextField(default="")),
                ("postComments", models.JSONField(null=True)),
                (
                    "userID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthScore.user",
                    ),
                ),
            ],
        ),
    ]
