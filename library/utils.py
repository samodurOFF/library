from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


def set_jwt_cookies(response, user):
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token

    timestamp = timezone.now().timestamp()  # текущее время эпохи UNIX
    access_expiry = access_token['exp'] - timestamp
    refresh_expiry = refresh_token['exp'] - timestamp

    response.set_cookie(
        key='access_token',
        value=str(access_token),
        httponly=True,
        secure=False,
        samesite='Lax',
        max_age=access_expiry
    )
    response.set_cookie(
        key='refresh_token',
        value=str(refresh_token),
        httponly=True,
        secure=False,
        samesite='Lax',
        max_age=refresh_expiry
    )



