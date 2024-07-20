from django.shortcuts import render
from .forms import CityForm
from .models import *
from .utils import get_weather
from django.conf import settings
from django.contrib.auth.decorators import login_required
import requests

from django.http import JsonResponse

def get_weather_view(request):
    form = CityForm()
    weather_data = None
    last_city = None

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            weather_data = get_weather(city_name)
            if weather_data and weather_data.get('cod') == 200:
                city_search, created = CitySearch.objects.get_or_create(city=city_name)
                city_search.search_count += 1
                city_search.save()

    else:
        city_name = request.GET.get('city', None)
        if city_name:
            weather_data = get_weather(city_name)
         
        

    search_history = CitySearch.objects.order_by('-last_searched')

    return render(request, 'index.html', {
        'form': form,
        'weather_data': weather_data,
        'search_history': search_history,
        'last_city': last_city,
    })


def city_autocomplete(request):
    if 'term' in request.GET:
        term = request.GET.get('term')
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={term}"
        
        
        try:
            response = requests.get(url)
            data = response.json()
            cities = []
            for item in data.get('results', []):
                city_name = item.get('name')
                country = item.get('country')
                if city_name and country:
                    cities.append(f"{city_name}, {country}")
                    
            return JsonResponse(cities, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        except ValueError:
            return JsonResponse({'error': 'Invalid JSON response'}, status=500)
    return JsonResponse([], safe=False)

