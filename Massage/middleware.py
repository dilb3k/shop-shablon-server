from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class JWTAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        try:
            query_string = scope.get('query_string', b'').decode()
            token = None
            for param in query_string.split('&'):
                if param.startswith('token='):
                    token = param.split('=')[1]
                    break

            if token:
                jwt_auth = JWTAuthentication()
                validated_token = await database_sync_to_async(jwt_auth.get_validated_token)(token)
                scope['user'] = await database_sync_to_async(jwt_auth.get_user)(validated_token)
            else:
                scope['user'] = AnonymousUser()
        except (InvalidToken, TokenError, KeyError):
            scope['user'] = AnonymousUser()

        return await self.app(scope, receive, send)

def JWTAuthMiddlewareStack(app):
    return JWTAuthMiddleware(AuthMiddlewareStack(app))