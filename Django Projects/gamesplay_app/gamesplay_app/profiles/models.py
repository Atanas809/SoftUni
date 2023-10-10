from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    MIN_AGE = 12
    MAX_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(MinValueValidator(MIN_AGE),),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

