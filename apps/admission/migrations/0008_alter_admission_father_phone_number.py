# Generated by Django 4.0.4 on 2022-04-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0007_alter_admission_father_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='father_phone_number',
            field=models.CharField(default='010', max_length=12),
        ),
    ]