from string import ascii_letters, digits

from django.core.exceptions import ValidationError


def validate_username(value):
    valid_chars = ascii_letters + digits + '_'

    for char in value:
        if char not in valid_chars:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
