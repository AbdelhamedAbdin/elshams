from django.db import models
from datetime import datetime

year = datetime.now().year

class EduLevel(models.Model):
    level = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.level


def create_albums(album_name, filename):
    return f"{year}/{album_name.education_level.level}/{filename}"


class Gallery(models.Model):
    education_level = models.ForeignKey(EduLevel, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to=create_albums)

    class Meta:
        ordering = ('-image',)

    def __str__(self):
        return str(self.education_level)

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
