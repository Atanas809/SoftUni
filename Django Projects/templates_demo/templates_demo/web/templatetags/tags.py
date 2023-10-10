from django.template import Library

from templates_demo.web.views import Student

register = Library()


@register.simple_tag(name='show_info')
def show_student_info(student: Student):
    return f'Hello, my info is: {student.get_info()}'


@register.simple_tag(name='sample_with_attr')
def sample_tag_with_multiple_attr(*args, **kwargs):
    return [str(x) for x in (list(args) + list(kwargs.values()))]


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,
    }

    return context
