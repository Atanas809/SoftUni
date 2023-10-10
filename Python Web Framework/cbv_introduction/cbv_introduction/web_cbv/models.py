from django.db import models
from django.urls import reverse


# Create your models here.


class Student(models.Model):
    class Meta:
        ordering = ('pk',)

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    age = models.PositiveIntegerField()

    def get_absolute_url(self):
        url = reverse('list view')

        return url
