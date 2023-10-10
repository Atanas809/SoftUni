from django.template import Library

from demo00.templates_introduction.views import Person

register = Library()


@register.simple_tag(name='get_info')
def get_person_info(person: Person):
    return f'My info is: {person.get_info()}'


@register.simple_tag(name='multiple_attrs')
def sample_tag_with_multiple_attrs(*args, **kwargs):
    output = ', '.join(str(x) for x in list(args) + list(kwargs.items()))
    return f'Simple tag with multiple attributes: {output}'


@register.simple_tag(name='peter_info')
def info_for_peter(person: Person):
    return f"My name is {person.name} and I'm {person.age} years old!"


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,
    }

    return context


@register.inclusion_tag('tags/numbers.html', name='gen_nums')
def generate_nums_list(values):
    context = {
        'nums': values
    }

    return context
