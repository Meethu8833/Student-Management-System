# Generated by Django 5.1.1 on 2025-01-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_classes_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='roll_number',
            field=models.IntegerField(auto_created=True),
        ),
    ]
