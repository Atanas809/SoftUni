from django.db import models
from django.urls import reverse

from demo01.core.validate_first_char_is_upper import first_upper


# Create your models here.

class DateInfo(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    last_modified = models.DateTimeField(
        auto_now=True,
    )


class City(DateInfo, models.Model):
    class Meta:
        verbose_name_plural = 'Cities'

    name = models.CharField(
        max_length=30,
        unique=True,
    )

    population = models.FloatField()

    postal_code = models.CharField(
        max_length=5,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        url = reverse(
            'city details',
            kwargs={'pk': self.pk, 'slug': self.slug},
        )

        return url


class School(DateInfo, models.Model):

    name = models.CharField(
        validators=[first_upper],
        max_length=40,
        unique=True,
    )

    city = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
    )

    slug = models.SlugField(
        unique=True,
    )

    def city_name(self):
        return self.city.name

    def get_absolute_url(self):
        url = reverse(
            'school details',
            kwargs={'pk': self.pk, 'slug': self.slug},
        )

        return url

    def __str__(self):
        return f'{self.name}'


class Student(DateInfo, models.Model):

    LEVELS = [
        ('Junior', 'Junior'),
        ('Mid', 'Mid'),
        ('Regular', 'Regular'),
        ('Senior', 'Senior'),
    ]

    class Meta:
        ordering = ['last_name', 'first_name']

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    age = models.PositiveIntegerField()

    level = models.CharField(
        max_length=30,
        choices=LEVELS,
    )

    good_grades = models.BooleanField(
        null=True,
    )

    school = models.ForeignKey(
        School,
        on_delete=models.RESTRICT,
    )

    slug = models.SlugField(
        unique=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def school_name(self):
        return self.school.name

    def __str__(self):
        return f'{self.full_name}'

    def get_absolute_url(self):
        url = reverse(
            'student details',
            kwargs={'slug': self.slug},
        )

        return url


class Address(DateInfo, models.Model):

    class Meta:
        verbose_name_plural = 'Address'

    name = models.CharField(
        max_length=30,
    )

    number = models.PositiveIntegerField()

    additional_info = models.TextField(
        null=True,
        blank=True,
    )

    city = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f'{self.name} {self.number}'
