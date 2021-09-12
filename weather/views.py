import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    city = 'London'
    appid = '01112e9f2a2bae82b21d8155e85ba84a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},&units=metric&appid=' + appid
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)
