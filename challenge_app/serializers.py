from rest_framework import serializers
import secrets

from .models import Redirect

class RedirectSerializer(serializers.ModelSerializer):
    '''
    Serializador para el modelo Redirect
    '''
    url = serializers.CharField(label="Ingrese URL", max_length=100)
    active = serializers.BooleanField(label="Activo")

    class Meta:
        model = Redirect
        fields = ['key', 'url', 'active', 'created_at', 'updated_at']
        read_only_fields = ['key', 'created_at', 'updated_at']

    def generate_unique_key(self):
        """
        Genera una clave unica para una instancia Redirect
        :return: Una clave unica
        """
        key = secrets.token_urlsafe(8)
        while Redirect.objects.filter(key=key).exists():
            key = secrets.token_urlsafe(8)
        return key

    def create(self, validated_data):
        """
        Crea una instancia de Redirect con una clave unica
        :param validated_data: diccionario de datos donde se envia los atributos que conformaran la instancia
        :return: Key del objeto creado
        """
        validated_data['key'] = self.generate_unique_key()
        return Redirect.objects.create(**validated_data)

    def update(self,  redirect_instance, validated_data):
        """
        Modifica y guarda una instancia de Redirect
        :param instance: Intancia que se modificara
        :param validated_data: diccionario de datos donde se envia los atributos que conformaran la instancia
        :return: una instancia de Redirect modificada
        """
        redirect_instance.url = validated_data.get('url',  redirect_instance.url)
        redirect_instance.active = validated_data.get('active',  redirect_instance.active)
        redirect_instance.save()
        return  redirect_instance

class GetUrlSerializer(serializers.Serializer):
    '''
    Serializador para la vista de GetUrl
    '''
    key = serializers.CharField()
    url = serializers.CharField()
