# Generated by Django 4.2.2 on 2024-11-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0004_course_owner_lesson_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                help_text="укажите курс",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="lms.course",
                verbose_name="курс",
            ),
        ),
    ]
