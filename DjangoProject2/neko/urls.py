from django.urls import path
from .views import get_neko_image

urlpatterns = [
    path('neko', get_neko_image, name='get_neko_image'),
]
