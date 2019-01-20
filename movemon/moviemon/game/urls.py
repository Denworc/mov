from sys import path

from django.conf.urls import url

from . import views

app_name = 'game'
urlpatterns = [
    url(r'^worldmap$', views.new_game, name='new-game'),
    url(r'^load_game$', views.load_game, name='load-game'),
    url(r'^', views.main_screen, name='main-screen'),
]