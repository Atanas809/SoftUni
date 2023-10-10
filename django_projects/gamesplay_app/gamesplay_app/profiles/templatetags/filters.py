from django.template import Library

register = Library()


@register.filter('format_to_first_decimal')
def format_rating(value):
    return f"{value:.1f}"
