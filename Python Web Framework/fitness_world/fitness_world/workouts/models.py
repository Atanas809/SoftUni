from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify


UserModel = get_user_model()


class Workout(models.Model):
    MAX_LEN_NAME = 40
    MIN_LEN_NAME = 3

    class Meta:
        ordering = ('-pk',)

    name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAME,),
        ),
    )

    reps = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    sets = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    link_to_image = models.URLField(
        max_length=500,
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

