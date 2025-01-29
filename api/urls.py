from django.urls import path
from .views import hng_api

urlpatterns = [
    path('', hng_api, name='hng_api'),
]
