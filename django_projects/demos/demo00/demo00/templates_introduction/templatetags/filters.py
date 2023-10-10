from django.template import Library

register = Library()


@register.filter('even')
def get_even_nums(values):
    return [x for x in values if x % 2 == 0]


@register.filter('even_names')
def get_even_names(names):
    return [x for x in names if len(x) % 2 == 0]


@register.filter('add_home')
def add_home(values):
    return [f"{x}'s home" for x in values]
