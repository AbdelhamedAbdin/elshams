# Generated by Django 4.0.4 on 2022-04-27 03:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
