from django.db import models


# Create your models here.

class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"