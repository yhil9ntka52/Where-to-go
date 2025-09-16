from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.places_list, name='places_list'),
    path('add/', views.add_place, name='add_place'),
    path('<int:pk>/', views.place_detail, name='place_detail'),
    path('choose/', views.choose_place_weighted, name='choose_place_weighted'),
]
