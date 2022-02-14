from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        import news.signals






