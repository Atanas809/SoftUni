from django.db import models
from django.urls import reverse

from demo002.core.phone_validator import validate_phone_number


# Create your models here.


class Course(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,
    )

    start_date = models.DateField()

    end_date = models.DateField()

    slug = models.SlugField(
        unique=True,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def get_absolute_url(self):
        url = reverse(
            'course info',
            kwargs={'pk': self.pk, 'slug': self.slug}
        )

        return url

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Undefined', 'Undefined'),
        )
    )

    email = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        validators=[validate_phone_number],
        max_length=10,
        unique=True,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.RESTRICT,
    )

    def get_absolute_url(self):
        url = reverse(
            'student info',
            kwargs={'pk': self.pk}
        )

        return url

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
