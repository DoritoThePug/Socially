"""
Code for overwriting default DRF TokenAuthentication to use HttpOnly cookie for token instead of Authorization header
"""

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _


def get_token_cookie(request):
    return request.COOKIES.get('token', None)


class CookieTokenAuthentication(TokenAuthentication):
    """
    Clients should authenticate by passing a Cookie named "token" in the request
    Token should have keywork "token " before the actual token, e.g.:
    "token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
    """

    model = Token

    def authenticate(self, request):
        token = get_token_cookie(request)

        if not token:
            msg = _("Token cookie not provided.")
            raise AuthenticationFailed(msg)

        token = token.split(' ')[1]
        return self.authenticate_credentials(token)

