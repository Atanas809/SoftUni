from django.template import Library

register = Library()


@register.filter('format_to_second_decimal')
def format_value(value):
    return f"{value:.2f}"
