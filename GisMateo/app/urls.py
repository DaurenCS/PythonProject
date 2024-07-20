from django.urls import path
from .views import *

urlpatterns = [
    path("weather", get_weather_view, name="get_weather"),
    path('city-autocomplete/', city_autocomplete, name='city-autocomplete'),
]
