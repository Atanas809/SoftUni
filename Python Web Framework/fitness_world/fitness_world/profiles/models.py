from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from fitness_world.core.mixins import ChoicesMixin


# Create your models here.

class Gender(ChoicesMixin):
    Male = 'Male'
    Female = 'Female'


class AppUser(auth_models.AbstractUser):
    MAX_LEN_NAMES = 20
    MIN_LEN_NAMES = 2

    first_name = models.CharField(
        max_length=MAX_LEN_NAMES,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAMES, ),
        ),
        error_messages={
            "min_length": f'First name must be grater than {MIN_LEN_NAMES} characters'
        }
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAMES,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_NAMES, ),
        ),
        error_messages={
            "min_length": f'Last name must be grater than {MIN_LEN_NAMES} characters'
        }
    )

    email = models.EmailField(
        unique=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=Gender.max_len(),
        choices=Gender.choices(),
        null=True,
        blank=True,
    )

    weight = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
