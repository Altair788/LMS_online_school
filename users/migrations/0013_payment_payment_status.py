# Generated by Django 4.2.2 on 2024-11-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_alter_payment_payment_method"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("pending", "Ожидает оплаты"),
                    ("paid", "Оплачено"),
                    ("failed", "Ошибка оплаты"),
                ],
                default="pending",
                help_text="укажите статус оплаты",
                max_length=20,
                verbose_name="статус оплаты",
            ),
        ),
    ]