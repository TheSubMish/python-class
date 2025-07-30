from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class SessionTimeoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
