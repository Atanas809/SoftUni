from django.http import HttpResponse
from django.shortcuts import render

from django101.tasks.models import Task


def home(request):
    context = {
        'db_data': Task.objects.all(),
    }

    return render(request, 'index.html', context)


def default_page(request):
    html = """
    <h1>This is default page</h1>
    <p>This is paragraph</p>
    """

    return HttpResponse(html)
