from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin

from user_django.auth_app.managers import AppUserManager


# Create your models here.


# class AppUser(User):
#     def has_first_name(self):
#         return self.first_name or 'First name is not specified!'
#
#     class Meta:
#         proxy = True


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    # Now user credentials consist of 'email' and 'password' not 'username' and 'password'
    USERNAME_FIELD = "email"

    objects = AppUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25
    )

    last_name = models.CharField(
        max_length=25
    )

    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
