from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from .models import Redirect

# Constantes

CACHE_TIMEOUT = 3600 # 3600 = 1 hora

@receiver(post_save, sender=Redirect)
def update_cache_on_redirect_save(sender, instance, **kwargs):
    """
    Actualiza la cache cuando se guarda un objeto Redirect con active en True y lo elimina si cambia a False
    """
    cache_key = instance.key
    # Intenta obtener los datos existentes en cache
    existing_data = cache.get(cache_key)
    if instance.active:
        # Si 'active' es True, actualiza la cache
        update_cache(instance)
    elif existing_data:
        # Si 'active' ha cambiado a False, elimina la entrada de la cache
        cache.delete(cache_key)

def update_cache(redirect_instance):
    """
    Actualiza la cache con los datos del objeto Redirect.
    """
    cache_key = str(redirect_instance.key)
    cache_data = {
        "key": redirect_instance.key,
        "url": redirect_instance.url,
    }
    # Guarda los datos en cache con un tiempo de expiracion.
    cache.set(cache_key, cache_data, timeout=CACHE_TIMEOUT )

