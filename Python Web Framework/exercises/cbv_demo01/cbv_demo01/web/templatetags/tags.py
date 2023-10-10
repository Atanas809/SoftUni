from django.template import Library


register = Library()


@register.inclusion_tag('partials/navigation.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,
    }

    return context
