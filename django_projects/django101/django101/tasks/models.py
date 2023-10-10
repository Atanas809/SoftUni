from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(
        max_length=30,
        null=False
    )

    text = models.CharField(
        max_length=60,
    )

    def __str__(self):
        return f"{self.id}: {self.title}"
