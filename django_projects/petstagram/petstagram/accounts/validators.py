from django.core.exceptions import ValidationError


def validate_only_alpha(value):
    if not value.isalpha():
        raise ValidationError("Field should contain only letters!")
