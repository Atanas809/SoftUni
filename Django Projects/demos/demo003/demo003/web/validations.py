from django.core.exceptions import ValidationError


def all_decimal(value):
    if not value.isdigit():
        raise ValidationError('Must contain only digits')
