from django.db import models

# Create your models here.


class Employee(models.Model):
    username = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    experience_years = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    good_skills = models.BooleanField(
        null=True,
    )

    def __str__(self):
        return self.username
