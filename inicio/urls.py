from .views import InicioView
from django.urls import path

app_name = 'inicio'

urlpatterns = [
    path('', InicioView, name='index')
]

