from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validations import validate_image
from petstagram.core.model_mixin import StrFieldsMixin


UserModel = get_user_model()


class Photo(StrFieldsMixin, models.Model):
    str_fields = ('id', 'photo')

    MIN_LENGTH_DESCRIPTION = 10
    MAX_LENGTH_DESCRIPTION = 300

    photo = models.ImageField(
        upload_to='images',
        validators=[validate_image],
        null=False,
        blank=False,
    )

    description = models.CharField(
        validators=[MinLengthValidator(MIN_LENGTH_DESCRIPTION)],
        max_length=MAX_LENGTH_DESCRIPTION,
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )