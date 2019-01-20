from sys import path

from django.conf.urls import url

from . import views

app_name = 'game'
urlpatterns = [
    url(r'^worldmap$', views.new_game, name='new-game'),
    url(r'^load_game$', views.load_game, name='load-game'),
    url(r'^save_game$', views.save_game, name='save-game'),
    url(r'^battle/(?P<pk>[0-9]+)$', views.battle, name='battle'),
    url(r'^moviedex$', views.moviedex, name='moviedex'),
    url(r'^moviedex/(?P<pk>[0-9]+)$', views.detail, name='detail'),
    url(r'^options$', views.options, name='options'),
    url(r'^$', views.main_screen, name='main-screen'),
]