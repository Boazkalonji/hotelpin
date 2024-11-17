from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'gestionhotel'

urlpatterns = [
    path('', index , name='index'),
    path('services', services , name='services'),
    path('index', index , name='index'),
    path('about', about , name='about'),
    path('galerie', galerie , name='galerie'),
    path('album_one', album_one , name='album_one'),
    path('album_deux', album_deux , name='album_deux'),
    path('contact', contact , name='contact'),
    
    

    

]