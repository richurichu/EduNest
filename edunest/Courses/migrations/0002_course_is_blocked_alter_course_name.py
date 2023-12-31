# Generated by Django 4.2.6 on 2023-10-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
