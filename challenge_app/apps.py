from django.apps import AppConfig


class ChallengeAppConfig(AppConfig):
    name = 'challenge_app'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        """
        Importa los signals
        """
        import challenge_app.signals