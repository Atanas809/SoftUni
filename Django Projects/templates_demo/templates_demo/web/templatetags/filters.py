from django.template import Library

register = Library()


@register.filter('odd')
def get_odd(values):
    return [x for x in values if x % 2 != 0]


@register.filter('app_date')
def filter_data(date):
    return date.strftime('%Y/%b/%d/%a')


@register.filter('incrementer')
def increment(values):
    return [x + 1 for x in values if x % 2 != 0]
