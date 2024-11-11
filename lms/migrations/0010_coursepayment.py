# Generated by Django 4.2.2 on 2024-11-10 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lms", "0009_alter_subscription_course_alter_subscription_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoursePayment",
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
                    "amount",
                    models.PositiveIntegerField(
                        help_text="укажите сумму оплаты", verbose_name="сумма оплаты"
                    ),
                ),
                (
                    "session_id",
                    models.CharField(
                        blank=True,
                        help_text="укажите идентификатор сессии",
                        max_length=255,
                        null=True,
                        verbose_name="идентификатор сессии",
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        help_text="укажите ссылку на оплату",
                        max_length=400,
                        null=True,
                        verbose_name="ссылка на оплату",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="укажите курс",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lms.course",
                        verbose_name="курс",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="укажите пользователя",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "оплата",
                "verbose_name_plural": "оплаты",
            },
        ),
    ]
