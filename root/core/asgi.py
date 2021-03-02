"""
ASGI config for root project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
#import chat.routing
from django.apps import apps

bokeh_app_config = apps.get_app_config('bokeh.server.django')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            bokeh_app_config.routes.get_websocket_urlpatterns()

        ),
    ),
    'http': AuthMiddlewareStack(URLRouter(bokeh_app_config.routes.get_http_urlpatterns())),
})

# import os

# import django
# from channels.routing import get_default_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_multi_apps.settings')
# django.setup()
# application = get_default_application()