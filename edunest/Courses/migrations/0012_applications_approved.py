# Generated by Django 4.2.6 on 2023-10-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0011_applications_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
