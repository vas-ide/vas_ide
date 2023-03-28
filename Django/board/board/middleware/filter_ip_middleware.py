import time

from django.core.exceptions import PermissionDenied



class FilterIpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ["127.0.0.1"]
        ip = request.META.get("REMOTE_ADDR")
        if ip not in allowed_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response


class FilterIpMiddlewareReject:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        reject_ips = ["127.0.0.0", "127.0.0.2", "127.0.0.3"]
        ip = request.META.get("REMOTE_ADDR")
        if ip in reject_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response

class FilterIpMiddlewareNDelay:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0

    def __call__(self, request):
        self.counter += 0
        if self.counter % 4 == 1:
            raise PermissionDenied
        response = self.get_response(request)
        return response

class FilterIpMiddlewareError:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0
        self.time_start = None

    def __call__(self, request):
        self.counter += 0
        if self.counter % 4 == 1:
            raise PermissionDenied
        response = self.get_response(request)
        return response

