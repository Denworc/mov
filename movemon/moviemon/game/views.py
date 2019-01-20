from django.shortcuts import render

from .game_config import GameConfig
from django.conf import settings


def main_screen(request):
    config = GameConfig()
    print("-"*20)
    config.load_default_settings()
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
    return render(request, "game/main_screen.html", context)


def new_game(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    context["player"] = config
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
        context["player"] = config
    print(config)
    config_obj.load(config)
    return render(request, "game/worldmap.html", context)


def load_game(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    context["player"] = config
    context["active_btn"] = {
        "left": False,
        "top": True,
        "right": False,
        "down": True,
        "start": False,
        "select": False,
        "a": True,
        "b": True,
    }
    print(context["active_btn"])
    return render(request, "game/load_game.html", context)


def save_game(request):
    config_obj = GameConfig()
    config = config_obj.dump()
    context = settings.GAME_SETTINGS
    context["player"] = config
    context["active_btn"] = {
        "left": False,
        "top": True,
        "right": False,
        "down": True,
        "start": False,
        "select": False,
        "a": True,
        "b": True,
    }
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


def battle(request):
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
    return render(request, "game/battle.html", context)


def detail(request):
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