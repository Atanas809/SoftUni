from django.db import models
from django.utils.text import slugify


# Create your models here.


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'

    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    created_on = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    MAX_NAME_LENGTH = 40

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
