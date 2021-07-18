from django.apps import AppConfig


class MenuAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu_app'

    def ready(self):
        from .crons import start_job
        start_job()
