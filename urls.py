from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'home'),
    path('create', views.create, name = 'create'),
    path('join', views.join, name = 'join'),
    path('registration', views.regi, name = 'regi'),
    path('login', views.login, name = 'login'),
]
