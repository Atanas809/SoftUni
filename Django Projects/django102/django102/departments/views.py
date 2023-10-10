from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.


def default_page(request):
    return HttpResponse('Hello from default page!')


def search_page_by_name(request, page_name, page_id):
    if page_id <= 10:
        context = {
            'page_name': page_name,
            'page_id': page_id,
        }

        return render(request, 'pages.html', context)

    return redirect('by-id', page_id)


def search_page_by_id(request, page_id):
    context = {
        'page_name': 'test',
        'page_id': page_id,
    }

    return render(request, 'pages.html', context)


def pages():
    valid = ['test', 'store', 'food', 'cars']

    return valid


def valid_pages(request):
    context = {
        'all_pages': pages(),
    }

    return render(request, 'show_valid_pages.html', context)


def go_to_page(request, page_name):
    valid_page_names = pages()

    if page_name not in valid_page_names:
        return HttpResponseNotFound("This page doesn't exist!")

    context = {
        'page_name': page_name,
        'page_data': 'test data',
    }

    return render(request, 'show_page.html', context)


def search_by_page(request, page):
    return redirect('go-to-page', page)
