from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


class Student(AbstractUser):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(30, ),
        ),
        error_messages={
            "min_length": f'First name must be grater than {30} characters'
        }
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(30, ),
        ),
        error_messages={
            "min_length": f'Last name must be grater than {30} characters'
        }
    )

    email = models.EmailField(
        unique=True,
    )
    age = models.PositiveIntegerField()


class Profile(models.Model):
    school = models.CharField(
        null=True,
        blank=True,
        max_length=45,
    )

    gender = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
        ),
    )

    is_good_student = models.BooleanField(
        null=True,
        blank=True,
    )

    student = models.OneToOneField(
        Student,
        primary_key=True,
        on_delete=models.CASCADE,
    )
