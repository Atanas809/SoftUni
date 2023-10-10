from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Profile(models.Model):
    MIN_AGE = 12
    MAX_LENGTH = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(MIN_AGE),),
        error_messages={
            'min_value': f"Age cannot be under {MIN_AGE}!",
        }
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
