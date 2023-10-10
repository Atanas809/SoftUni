from django.contrib.auth import get_user_model
from django.db import models

from fitness_world.photos.models import Photo

UserModel = get_user_model()


class LikePhoto(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class CommentPhoto(models.Model):
    class Meta:
        ordering = ('-publication_date',)

    MAX_TEXT_LENGTH = 200

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f"Comment {self.pk}: {self.text}"
