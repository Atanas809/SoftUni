from django.db import models

from gamesplay_app.games.validators import rating_range


# Create your models here.


class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    CATEGORIES = (
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
        max_length=MAX_LEN_TITLE,
    )

    category = models.CharField(
        null=False,
        blank=False,
        choices=CATEGORIES,
        max_length=MAX_LEN_CATEGORY,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(rating_range,),
    )

    max_level = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
