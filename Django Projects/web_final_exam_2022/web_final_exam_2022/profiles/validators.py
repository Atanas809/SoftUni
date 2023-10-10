from django.core.exceptions import ValidationError


def validate_username(value):
    min_length = 2

    if len(value) < 2:
        raise ValidationError(f"The username must be a minimum of {min_length} chars")
