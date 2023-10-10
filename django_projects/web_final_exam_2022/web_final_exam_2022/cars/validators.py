from django.core.exceptions import ValidationError


def validate_model(value):
    min_length = 2

    if len(value) < 2:
        raise ValidationError(f'Model must be greater than {min_length} characters')


def validate_year_in_range(value):
    min_year = 1980
    max_year = 2049

    if value < min_year or value > max_year:
        raise ValidationError(f"Year must be between {min_year} and {max_year}")
