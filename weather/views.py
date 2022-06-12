from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import environ


env = environ.Env()
environ.Env.read_env()


def weather(req, city):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=pt_br&units=metric&appid={}'
	city_weather = requests.get(url.format(city, env("OPEN_WEATHER_KEY"))).json()
	
	if city_weather['cod'] == '404':
		messages.add_message(req, messages.INFO, 'Cidade não encontrada')
		return redirect('choose_city')

	news_brasil = requests.get(f'https://api.worldnewsapi.com/search-news?number=6&language=pt&source-countries=br&text=tesla&api-key={env("NEWS_KEY")}').json()
	
	context = {
		'weather': city_weather,
		'news_brasil': news_brasil,
	}
	
	return render(req, 'weather.html', context)


def choose_city(req):
	city = req.GET.get('city')
	
	if not city:
		return render(req, 'choose_city.html')
	else:
		# don't need to verify if it's valid, bc the weather view will
		# redirect to this view if there is none
		return redirect('weather', city)

# 6 do brasil e 3 global ???
# https://api.worldnewsapi.com/search-news?number=9&language=pt&source-countries=br&text=tesla&api-key=env("NEWS_KEY")
# earliest-publish-date
