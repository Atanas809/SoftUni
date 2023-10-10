from django.core.validators import MinLengthValidator
from django.db import models

from prep_exam01.profiles.validators import validate_username


# Create your models here.

class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15

    username = models.CharField(
        null=False,
        blank=False,
        validators=(MinLengthValidator(MIN_LEN_USERNAME), validate_username,),
        max_length=MAX_LEN_USERNAME,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
