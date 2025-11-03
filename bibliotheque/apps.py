from django.apps import AppConfig


class BibliothequeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bibliotheque'

    def ready(self):
        import bibliotheque.signals  
        
        
