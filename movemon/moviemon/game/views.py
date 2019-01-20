from django.shortcuts import render

from .game_config import GameConfig
from django.conf import settings
import urllib.request, json
from random import randint


def main_screen(request):
    config = GameConfig()
    config.load_default_settings()
    config_red = config.dump()
    titles = [
        'monster',
        'zombie',
        'creepy',
        'pokemon',
		'chupacabra',
		'ghost',
		'shrek',
		'alien',
		'frankenstein',
		'phantom',
		'devil',
		'sponge bob',
		'shark',
		'werewolf',
		'hodag',
		'dybbuk',
		'wyvern',
		'cerberus',
		'windigo',
		'nix'
    ]

    for x in range(10):
        with urllib.request.urlopen(
                "http://www.omdbapi.com/?apikey=8176f978&t={}&plot=short&r=json".format(titles[randint(0, len(titles) - 1)])) as url:
            data = json.loads(url.read().decode())
        config_red["films"][x] = data
    print(config_red)
    context = settings.GAME_SETTINGS
    context["active_btn"] = {
        "left": False,
        "top": False,
        "right": False,
        "down": False,
        "start": False,
        "select": False,
        "a": True,
        "b": True,
    }
    config.load(config_red)
    return render(request, "game/main_screen.html", context)


def new_game(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    context["player"] = config
    context["msg"] = {
        "battle": False,
        "ball": False
    }
    context["active_btn"] = {
            "left": True,
            "top": True,
            "right": True,
            "down": True,
            "start": True,
            "select": True,
            "a": True,
            "b": False,
        }
    random = randint(0,3)
    if random == 0:
        config['balls_count'] += 1
        context["msg"]['ball'] = True
    elif random == 1:
        config['bettle_monster'] = config_obj.get_random_movie()
        context["msg"]['battle'] = True
    if request.method == 'POST':
        btn = request._get_post()['btn']
        if btn == "left" and config['position']['x'] > 0:
            config['position']['x'] -= 1
        elif btn == "top" and config['position']['y'] > 0:
            config['position']['y'] -= 1
        elif btn == "right" and config['position']['x'] < (settings.BLOCK_COUNT - 1):
            config['position']['x'] += 1
        elif btn == "down" and config['position']['y'] < (settings.BLOCK_COUNT - 1):
            config['position']['y'] += 1
        if config['position']['x'] == 0:
            context["active_btn"]['left'] = False
        if config['position']['x'] == 9:
            context["active_btn"]['right'] = False
        if config['position']['y'] == 0:
            context["active_btn"]['top'] = False
        if config['position']['y'] == 9:
            context["active_btn"]['down'] = False
        if not context["msg"]['battle']:
            context["active_btn"]['a'] = False
        context["player"] = config
    config_obj.load(config)
    return render(request, "game/worldmap.html", context)


def load_game(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    if request.method == 'POST':
        btn = request._get_post()['btn']
        if btn == "top" and config['chosen_l']['load_one']:
            config['chosen_l']['load_one'] = False
            config['chosen_l']['load_three'] = True
        elif btn == "top" and config['chosen_l']['load_two']:
            config['chosen_l']['load_one'] = True
            config['chosen_l']['load_two'] = False
        elif btn == "top" and config['chosen_l']['load_three']:
            config['chosen_l']['load_three'] = False
            config['chosen_l']['load_two'] = True
        elif btn == "down" and config['chosen_l']['load_three']:
            config['chosen_l']['load_one'] = True
            config['chosen_l']['load_three'] = False
        elif btn == "down" and config['chosen_l']['load_two']:
            config['chosen_l']['load_three'] = True
            config['chosen_l']['load_two'] = False
        elif btn == "down" and config['chosen_l']['load_one']:
            config['chosen_l']['load_two'] = True
            config['chosen_l']['load_one'] = False
        else:
            config['chosen_l']['load_three'] = True
    context["player"] = config
    context["active_btn"] = {
        "left": False,
        "top": True,
        "right": False,
        "down": True,
        "start": False,
        "select": False,
        "a": False,
        "b": True,
    }
    config_obj.load(config)
    return render(request, "game/load_game.html", context)


def save_game(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    if request.method == 'POST':
        btn = request._get_post()['btn']
        if btn == "top" and config['chosen_l']['load_one']:
            config['chosen_l']['load_one'] = False
            config['chosen_l']['load_three'] = True
        elif btn == "top" and config['chosen_l']['load_two']:
            config['chosen_l']['load_one'] = True
            config['chosen_l']['load_two'] = False
        elif btn == "top" and config['chosen_l']['load_three']:
            config['chosen_l']['load_three'] = False
            config['chosen_l']['load_two'] = True
        elif btn == "down" and config['chosen_l']['load_three']:
            config['chosen_l']['load_one'] = True
            config['chosen_l']['load_three'] = False
        elif btn == "down" and config['chosen_l']['load_two']:
            config['chosen_l']['load_three'] = True
            config['chosen_l']['load_two'] = False
        elif btn == "down" and config['chosen_l']['load_one']:
            config['chosen_l']['load_two'] = True
            config['chosen_l']['load_one'] = False
        else:
            config['chosen_l']['load_three'] = True
    context["player"] = config
    context["active_btn"] = {
        "left": False,
        "top": True,
        "right": False,
        "down": True,
        "start": False,
        "select": False,
        "a": False,
        "b": True,
    }
    config_obj.load(config)
    return render(request, "game/save.html", context)


def options(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    context["player"] = config
    context["active_btn"] = {
        "left": False,
        "top": False,
        "right": False,
        "down": False,
        "start": True,
        "select": False,
        "a": True,
        "b": True,
    }
    return render(request, "game/options.html", context)


def battle(request, pk):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    context["player"] = config
    context["active_btn"] = {
        "left": False,
        "top": False,
        "right": False,
        "down": False,
        "start": False,
        "select": False,
        "a": True,
        "b": True,
    }
    if context["player"]["balls_count"] < 2:
        context["active_btn"]['a'] = False
    if request.method == 'POST':
        btn = request._get_post()['btn']
        if btn == "a":
            print(config['balls_count'])
            config['balls_count'] -= 1
    config_obj.load(config)
    context["film"] = config_obj.get_movie(pk)
    return render(request, "game/battle.html", context)


def detail(request, pk):
    context = {
        "active_btn": {
            "left": False,
            "top": False,
            "right": False,
            "down": False,
            "start": False,
            "select": False,
            "a": False,
            "b": True,
        }
    }
    return render(request, "game/detail.html", context)


def moviedex(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    context["player"] = config
    context["active_btn"] = {
        "left": True,
        "top": False,
        "right": True,
        "down": False,
        "start": False,
        "select": True,
        "a": True,
        "b": False,
    }
    return render(request, "game/moviedex.html", context)