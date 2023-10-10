from django.template import Library

register = Library()


@register.filter('placeholder')
def set_placeholders(value, name):
    value.field.widget.attrs['placeholder'] = name

    return value
