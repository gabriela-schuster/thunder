from django.urls import path
from . import views


urlpatterns = [
	path('cidade/', views.choose_city, name='choose_city'),
	path('<str:city>/', views.weather, name='weather'),
]
