from django.db import models

# Create your models here.


class Note(models.Model):
    class Meta:
        ordering = ('pk',)

    MAX_LEN_TITLE = 30

    title = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_TITLE,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )
