import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):
    appid = '01112e9f2a2bae82b21d8155e85ba84a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
