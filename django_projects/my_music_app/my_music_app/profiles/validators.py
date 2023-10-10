from string import ascii_letters, digits

from django.core.exceptions import ValidationError


def validate_username(value):
    all_letters = ascii_letters
    all_digits = digits

    can_contain = all_letters + all_digits + '_'

    for char in value:
        if char not in can_contain:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
