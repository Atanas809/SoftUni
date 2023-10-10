def number_starts_with_zero(value):
    if value[0] != '0':
        raise ValueError("Invalid phone number!")


def is_valid_length(value):
    if len(value) < 10 or len(value) > 10:
        raise ValueError("Invalid phone number!")


def contains_only_numbers(value):
    if not value.isdigit():
        raise ValueError("Invalid phone number!")
