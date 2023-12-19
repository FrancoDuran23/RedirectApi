from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.cache import cache

from .models import Redirect
from .serializers import RedirectSerializer, GetUrlSerializer
from .signals import update_cache

class RedirectView(generics.ListCreateAPIView):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer

class RedirectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer

    def get_object(self, key):
        """
        :param key: Clave de instancia
        :return: Devuelve la instancia o 404 en caso de no existir
        """
        try:
            return Redirect.objects.get(key=key)
        except Redirect.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = RedirectSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = RedirectSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUrlView(APIView):
    def get(self, request, key, **kwargs):
        '''
        Busca en cache el url, de no existir y estar activo en la bd, actualiza el cache

        '''
        if key is not None:
            # Intentar obtener el valor desde cache
            cached_data = cache.get(key)
            if cached_data is not None:
                return Response(cached_data)
            else:
                try:
                    # Buscar en la base de datos el objeto con la clave proporcionada
                    redirect_instance = Redirect.objects.get(key=key)
                    if redirect_instance.active:
                        serializer = GetUrlSerializer(redirect_instance)
                        # Obtener los datos serializados
                        response_data = serializer.data
                        # Guardar la respuesta en la caché
                        update_cache(redirect_instance)
                        return Response(response_data)
                    else:
                        return Response({"error": "No se encontró ninguna URL activa para la clave proporcionada"}, status=status.HTTP_404_NOT_FOUND)
                except Redirect.DoesNotExist:
                    # Si no se encuentra el objeto, devolver un JSON indicando que no se encontro
                    return Response({"error": "No se encontró ninguna URL para la clave proporcionada"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Si no se proporciona la clave en la solicitud, devolver un JSON indicando el error
            return Response({"error": "Se requiere el parámetro 'key' en la solicitud GET"}, status=status.HTTP_400_BAD_REQUEST)