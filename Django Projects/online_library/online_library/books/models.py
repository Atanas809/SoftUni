from django.db import models


# Create your models here.

class Book(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_TYPE = 30

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    book_type = models.CharField(
        max_length=MAX_LEN_TYPE,
        null=False,
        blank=False,
        verbose_name='Type'
    )
