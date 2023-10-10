from django.core.exceptions import ValidationError


def first_upper(value):
    if value[0].islower():
        raise ValidationError('First char must be upper')
