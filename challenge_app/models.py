from django.db import models

# Constantes

MAX_LENGTH = 255

# Modelos.

class Redirect(models.Model):
    '''
    Modelo de Redirect
    '''
    key = models.CharField(max_length=MAX_LENGTH, unique=True)
    url = models.CharField(max_length=MAX_LENGTH )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key