# Generated by Django 4.0.4 on 2022-05-15 10:05

import apps.gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_gallery_options_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(height_field='570', upload_to=apps.gallery.models.create_albums, width_field='440'),
        ),
    ]