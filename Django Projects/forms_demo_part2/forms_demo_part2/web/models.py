from django.core import validators
from django.db import models

from forms_demo_part2.web.validators import ValueInRangeValidator


# Create your models here.

class Type(models.Model):
    name = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.name


class Animal(models.Model):
    MAX_LEN_NAME = 40
    MAX_LEN_TYPE = 30

    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    type = models.ForeignKey(
        Type,
        on_delete=models.RESTRICT,
    )

    age = models.IntegerField(
        validators=(ValueInRangeValidator(1, 20),),
        null=True,
    )
