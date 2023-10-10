from django.db import models
from django.utils.text import slugify

from demo003.web.validations import all_decimal


# Create your models here.


class Course(models.Model):
    name = models.CharField(
        max_length=50,
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    last_modified = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(
        max_length=30,
    )

    age = models.PositiveIntegerField(
        default=0,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    personal_info = models.CharField(
        validators=(all_decimal,),
        max_length=10,
        unique=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    courses = models.ManyToManyField(
        Course,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.personal_info}")

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
