"""
ASGI config for root project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.asgi import get_asgi_application
django_asgi = get_asgi_application()

from channels.routing import get_default_application
from django.urls import path, re_path
#from api.schema import MyGraphqlWsConsumer
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import ChatConsumer
from django.apps import apps

channels_asgi = get_default_application()

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # bokeh_app_config.routes.get_websocket_urlpatterns()
            #[path("api/graphql/", MyGraphqlWsConsumer.as_asgi()),
             [re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi())
             ]
        ),
    ),
    'http': AuthMiddlewareStack(URLRouter(
        [re_path(r"", channels_asgi)]))  # bokeh_app_config.routes.get_http_urlpatterns())),
})

# import os

# import django
# from channels.routing import get_default_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_multi_apps.settings')
# django.setup()
# application = get_default_application()
