# Generated by Django 4.0.4 on 2022-04-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_alter_admission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='is_joined_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
