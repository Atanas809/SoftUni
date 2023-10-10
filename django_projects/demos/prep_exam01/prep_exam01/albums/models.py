from enum import Enum

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name.replace('_', ' '), x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    Pop_Music = 'Pop Music'
    Jazz_Music = 'Jazz Music'
    RNB_Music = 'R&B Music'
    Rock_Music = 'Rock Music'
    Country_Music = 'Country Music'
    Dance_Music = 'Dance Music'
    Hip_Hop_Music = 'Hip Hop Music'
    Other = 'Other'


class Album(models.Model):
    MAX_LEN = 30

    class Meta:
        ordering = ('pk', )

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_LEN,
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN,
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN,
        choices=AlbumGenres.choices(),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(0.0),)
    )
