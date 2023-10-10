from django.core.validators import MinLengthValidator
from django.db import models

from exercises_for_web.pets.models import Pet
from exercises_for_web.photos.validations import validate_image_size

"""
The fields description and tagged pets are optional:

· Description - a user can write any description of the photo; it should consist of a maximum of 300 characters and a minimum of 10 characters

· Location - it should consist of a maximum of 30 characters

· Tagged Pets - the user can tag none, one, or many of all pets. There is no limit on the number of tagged pets

There should be created one more field that will be automatically generated:

· Date of publication - when a picture is added or edited, the date of publication is automatically generated
"""
# Create your models here.


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='images',
        validators=(validate_image_size,),
        null=False,
        blank=False,
    )

    description = models.CharField(
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.pk}-->{self.photo}"
