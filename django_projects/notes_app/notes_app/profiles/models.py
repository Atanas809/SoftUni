from django.db import models


# Create your models here.


class Profile(models.Model):
    MAX_LEN_NAME = 20

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
