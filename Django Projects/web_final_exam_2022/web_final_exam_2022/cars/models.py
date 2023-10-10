from django.core.validators import MinValueValidator
from django.db import models

from web_final_exam_2022.cars.validators import validate_model, validate_year_in_range


# Create your models here.


class Car(models.Model):
    class Meta:
        ordering = ('pk',)

    VALID_CAR_TYPES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    car_type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=VALID_CAR_TYPES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(validate_model,)
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(validate_year_in_range,)
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(1),),
    )
