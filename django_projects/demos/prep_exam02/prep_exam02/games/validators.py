from django.core.exceptions import ValidationError


def validate_rating_in_range(value):
    min_value = 0.1
    max_value = 5

    if value < min_value or value > max_value:
        raise ValidationError(f"Value must be between {min_value} and {max_value}!")
