from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from petstagram.core.model_mixin import StrFieldsMixin
# Create your models here.

UserModel = get_user_model()


class Pet(models.Model):
    str_fields = ('name', 'pk')
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
