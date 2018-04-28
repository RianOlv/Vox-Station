from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('signup/', views.NewContaView, name='NewConta'),
    path('login/', views.LoginView, name='LoginConta'),
]
