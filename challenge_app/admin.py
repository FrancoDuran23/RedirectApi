from django.contrib import admin
from .models import Redirect

# Modelos Admin

class RedirectAdmin(admin.ModelAdmin):
    '''
    Custom Admin model para Redirect
    '''
    list_display = ('key', 'url', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'created_at')
    search_fields = ('key', 'url')

# Registro del modelo

admin.site.register(Redirect, RedirectAdmin)