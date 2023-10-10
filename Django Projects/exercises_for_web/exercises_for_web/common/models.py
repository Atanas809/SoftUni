from django.db import models

from exercises_for_web.photos.models import Photo


# Create your models here.


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f"Comment: {self.text}"


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
