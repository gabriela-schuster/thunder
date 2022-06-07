from django.shortcuts import render
import requests
import environ


env = environ.Env()
environ.Env.read_env()


def home(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=pt_br&units=metric&appid={}'
	city = 'encantado'
	city_weather = requests.get(url.format(city, env("OPEN_WEATHER_KEY"))).json()
	context = {
		'weather': city_weather,
	}
	
	return render(request, 'home.html', context)

# 48dd17cf60c2ced81f4e2bbaf9cfb1c2
