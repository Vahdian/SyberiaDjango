
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('', views.login, name="login"),
    path('', views.logout, name="logout"),
    
]