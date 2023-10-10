from enum import Enum

from django.db import models

from my_music_app.albums.validators import price_fixer


# Create your models here.

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoiceEnum):
    Pop = 'Pop Music'
    Jazz = 'Jazz Music'
    RNB = 'R&B Music'
    Rock = 'Rock Music'
    Country = 'Country Music'
    Dance = 'Dance Music'
    Hip_Hop = 'Hip Hop Music'
    Other = 'Other'


class Album(models.Model):
    MAX_LEN_FIELD = 30

    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=MAX_LEN_FIELD,
    )

    artist = models.CharField(
        max_length=MAX_LEN_FIELD,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_FIELD,
        choices=AlbumGenres.choices(),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        validators=(price_fixer,),
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)
