from django.core.exceptions import ValidationError


def password_check(passwd):
    special_symbols = ['$', '@', '#', '%']
    min_length = 6
    max_length = 20

    if len(passwd) < 6:
        raise ValidationError(f'length should be at least {min_length}')

    if len(passwd) > 20:
        raise ValidationError(f'length should be not be greater than {max_length}')

    if not any(char.isdigit() for char in passwd):
        raise ValidationError('Password should have at least one numeral')

    if not any(char.isupper() for char in passwd):
        raise ValidationError('Password should have at least one uppercase letter')

    if not any(char.islower() for char in passwd):
        raise ValidationError('Password should have at least one lowercase letter')

    if not any(char in special_symbols for char in passwd):
        raise ValidationError(f"Password should have at least one of the symbols {''.join(special_symbols)}")
