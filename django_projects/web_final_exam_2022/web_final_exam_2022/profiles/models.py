from django.core.validators import MinValueValidator
from django.db import models

from web_final_exam_2022.profiles.validators import validate_username


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(validate_username,)
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(18),)
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
