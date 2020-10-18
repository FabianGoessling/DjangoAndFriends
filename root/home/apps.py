from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'

    def ready(self):
        from home import signals  # noqa
