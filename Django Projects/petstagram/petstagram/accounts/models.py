from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from petstagram.accounts.validators import validate_only_alpha
from petstagram.core.model_mixin import ChoicesMixin


class Gender(ChoicesMixin):
    Male = 'Male'
    Female = 'Female'
    Do_Not_Show = 'Do Not Show'


class AppUser(AbstractUser):
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_FIRST_NAME = 2

    MAX_LEN_LAST_NAME = 30
    MIN_LEN_LAST_NAME = 2

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME, validate_only_alpha, ),
        )
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME, validate_only_alpha, ),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    gender = models.CharField(
        max_length=Gender.max_len(),
        choices=Gender.choices(),
    )

    image = models.ImageField(
        upload_to='staticfiles/images/',
        null=True,
        blank=True
    )
