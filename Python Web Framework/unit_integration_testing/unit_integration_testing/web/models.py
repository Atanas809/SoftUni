from django.core import validators
from django.db import models

from unit_integration_testing.web.validators import egn_validator


class Profile(models.Model):
    name = models.CharField(
        max_length=30,
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(0),
            validators.MaxValueValidator(150),
        ),
    )

    egn = models.CharField(
        max_length=10,
        validators=(
            egn_validator,
        ),
    )

    def __str__(self):
        return self.name
