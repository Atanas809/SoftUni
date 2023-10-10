from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from fitness_world.workouts.models import Workout


UserModel = get_user_model()


class Photo(models.Model):
    class Meta:
        ordering = ('-date_of_publication',)

    MAX_LEN_LOCATION = 30
    MIN_LEN_LOCATION = 3

    image = models.ImageField(
        upload_to='images/',
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LOCATION,),
        ),
        null=True,
        blank=True,
    )

    caption = models.TextField(
        null=True,
        blank=True,
    )

    music_link = models.URLField(
        null=True,
        blank=True,
    )

    workout = models.ManyToManyField(
        Workout,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    date_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.image}"