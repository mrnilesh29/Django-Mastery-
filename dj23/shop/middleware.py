import datetime

from django.utils.deprecation import MiddlewareMixin


class ShoplogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        now = datetime.datetime.now()
        print(f'{now} this is the current time requet url {request.path}')

    def process_response(self, request, response):
        now = datetime.datetime.now()
        print(f'{now} this is the current time response url {response.status_code} {request.path}')
        return response

class BlockingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("block page")