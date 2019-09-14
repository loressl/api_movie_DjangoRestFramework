from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('movies/', views.movies),
    path('actors/', views.actors),
]