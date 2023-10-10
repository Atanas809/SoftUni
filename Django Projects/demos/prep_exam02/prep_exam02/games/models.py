from enum import Enum

from django.core.validators import MinValueValidator
from django.db import models

from prep_exam02.games.validators import validate_rating_in_range


# Create your models here.


class Game(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 15
    MIN_LEVEL = 1

    VALID_CATEGORIES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )

    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_TITLE_LENGTH,
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CATEGORY_LENGTH,
        choices=VALID_CATEGORIES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(validate_rating_in_range,)
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(MIN_LEVEL),),
        error_messages={
            'min_value': f'Level cannot be below {MIN_LEVEL}!'
        }
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
