from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('download_report/<str:location>/', views.download_report, name='download_report'),
    path('map/', views.map_view, name='map_view'),
    path('get_weather_by_coordinates/', views.get_weather_by_coordinates, name='get_weather_by_coordinates'),
    path('city-suggestions/', views.city_suggestions, name='city_suggestions'),
]