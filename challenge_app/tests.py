from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Redirect
from .serializers import RedirectSerializer, GetUrlSerializer

class RedirectTests(TestCase):
    '''
    Conjunto de pruebas para el modelo Redirect
    '''
    def setUp(self):
        self.client = APIClient()
        self.redirect_data = {'url': 'https://example.com', 'active': True}

    def test_create_redirect(self):
        '''
        Test de creacion de instancia de Redirect
        '''
        url = reverse('redirect')
        response = self.client.post(url, self.redirect_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_redirect_detail(self):
        '''
        Test de detalle de una instancia de Redirect
        '''
        # Creacion de instancia
        serializer = RedirectSerializer(data=self.redirect_data)
        serializer.is_valid()
        redirect_instance = serializer.save()

        url = reverse('redirect-detail', args=[redirect_instance.key])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], 'https://example.com')

class GetUrlViewTests(TestCase):
    '''
    Conjunto de pruebas para la vista de GetURl
    '''
    def setUp(self):
        self.client = APIClient()
        # Creacion de instancia con active en True
        self.redirect_data_active = {'url': 'https://example.com', 'active': True}
        serializer_active = RedirectSerializer(data=self.redirect_data_active)
        serializer_active.is_valid()
        self.redirect_instance_active = serializer_active.save()
        # Creacion de instancia con activo en False
        self.redirect_data_inactive = {'url': 'https://examplefalse.com', 'active': False}
        serializer_inactive = RedirectSerializer(data=self.redirect_data_inactive)
        serializer_inactive.is_valid()
        self.redirect_instance_inactive = serializer_inactive.save()

    def test_get_url_view_active(self):
        '''
        Test de creacion de instancia en true y busqueda de url
        '''
        response = self.client.get(reverse('get_url', args=[self.redirect_instance_active.key]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], 'https://example.com')

    def test_get_url_view_inactive(self):
        '''
        Test de creacion de instancia en false (no debe existir)
        '''
        response = self.client.get(reverse('get_url', args=[self.redirect_instance_inactive.key]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'No se encontró ninguna URL activa para la clave proporcionada')
