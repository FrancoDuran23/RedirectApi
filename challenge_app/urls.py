from django.urls import path
from .views import RedirectView, RedirectDetailView, GetUrlView

urlpatterns = [
    path('redirect/', RedirectView.as_view(), name='redirect'),
    path('redirect/<str:pk>/', RedirectDetailView.as_view(), name='redirect-detail'),
    path('get_url/<str:key>/', GetUrlView.as_view(), name='get_url'),
]