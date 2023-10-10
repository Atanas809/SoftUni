from django.core.exceptions import ValidationError


def validate_review_length(value):
    min_len = 4
    max_len = 40

    if len(value) <= min_len or len(value) > max_len:
        raise ValidationError(f'Text must be between {min_len} and {max_len} chars long!')
