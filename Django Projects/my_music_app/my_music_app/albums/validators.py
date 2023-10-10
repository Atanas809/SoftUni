from django.core.exceptions import ValidationError


def price_fixer(value):
    min_value = 0.0

    if value < min_value:
        raise ValidationError(f'The price cannot be below {min_value}.')
