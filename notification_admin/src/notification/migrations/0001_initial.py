# Generated by Django 4.0.4 on 2023-08-03 17:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL("""CREATE SCHEMA IF NOT EXISTS "notification";"""),
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.SlugField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                ("value", models.CharField(max_length=255, verbose_name="value")),
            ],
            options={
                "verbose_name": "config",
                "verbose_name_plural": "configs",
                "db_table": 'notification"."configs',
            },
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "transport_type",
                    models.CharField(
                        choices=[("email", "email"), ("websocket", "websocket"), ("sms", "sms")],
                        max_length=100,
                        verbose_name="transport_type",
                    ),
                ),
                (
                    "task",
                    models.CharField(
                        choices=[
                            ("set_rating", "Set Rating"),
                            ("user_registered", "User Registered"),
                            ("mass_sending", "Mass Sending"),
                        ],
                        max_length=100,
                        verbose_name="task",
                    ),
                ),
                ("theme", models.TextField(blank=True, null=True, verbose_name="theme")),
                ("template_body", models.TextField(verbose_name="template_body")),
            ],
            options={
                "verbose_name": "template",
                "verbose_name_plural": "templates",
                "db_table": 'notification"."templates',
            },
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "template_params",
                    models.TextField(blank=True, null=True, verbose_name="template_params"),
                ),
                (
                    "group",
                    models.CharField(
                        choices=[("subscribers", "subscribers"), ("everyone", "everyone")],
                        max_length=100,
                        verbose_name="group",
                    ),
                ),
                (
                    "timing",
                    models.CharField(
                        choices=[("one", "one"), ("week", "week"), ("month", "month")],
                        max_length=100,
                        verbose_name="timing",
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[("high", "high"), ("medium", "medium"), ("low", "low")],
                        max_length=100,
                        verbose_name="priority",
                    ),
                ),
                (
                    "last_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="last_date"),
                ),
                (
                    "planned_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="planned_date"),
                ),
                ("urgent", models.BooleanField(verbose_name="urgent")),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="notification.template",
                        verbose_name="template_schedule",
                    ),
                ),
            ],
            options={
                "verbose_name": "schedule",
                "verbose_name_plural": "schedules",
                "db_table": 'notification"."schedules',
            },
        ),
    ]
