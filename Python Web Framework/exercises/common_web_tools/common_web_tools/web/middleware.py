from django.utils import timezone


def number_of_visitors_middleware(get_response):
    def middleware(request, *args, **kwargs):
        response = get_response(request, *args, **kwargs)

        number_of_visits = request.session.get('VISITS_SESSION_KEY', 0) + 1
        request.session['VISITS_SESSION_KEY'] = number_of_visits

        return response

    return middleware


class MeasureTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        return self._middleware(request, *args, **kwargs)

    def _middleware(self, request, *args, **kwargs):
        start_time = timezone.now()

        response = self.get_response(request, *args, **kwargs)

        end_time = timezone.now()

        print(f"Execution time: {end_time - start_time}")

        return response
