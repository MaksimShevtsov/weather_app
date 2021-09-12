from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    city = 'London'
    appid = '01112e9f2a2bae82b21d8155e85ba84a'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},&appid={appid}'


    return render(request, 'weather/index.html')
