# Generated by Django 5.0.6 on 2024-08-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0003_alter_attendance_attendance_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_time',
            field=models.DateTimeField(),
        ),
    ]
