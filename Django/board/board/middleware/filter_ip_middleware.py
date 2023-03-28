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
        allowed_ips = ["127.0.0.0", "127.0.0.2", "127.0.0.3"]
        ip = request.META.get("REMOTE_ADDR")
        if ip in allowed_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response

class FilterIpMiddlewareNDelay:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ["127.0.0.1"]
        ip = request.META.get("REMOTE_ADDR")
        if ip not in allowed_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response

class FilterIpMiddlewareError:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ["127.0.0.1"]
        ip = request.META.get("REMOTE_ADDR")
        if ip not in allowed_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response

