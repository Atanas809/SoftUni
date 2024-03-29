from django.core.exceptions import ValidationError


def egn_validator(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError("EGN must contain exactly 10 digits!")
