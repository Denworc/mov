from django.shortcuts import render

from .game_config import GameConfig
from django.conf import settings


def main_screen(request):
    config = GameConfig()
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
            "start": False,
            "select": False,
            "a": True,
            "b": True,
        }
    return render(request, "game/worldmap.html", context)


def load_game(request):
    context = {
        "active_btn": {
            "left": False,
            "top": True,
            "right": False,
            "down": True,
            "start": False,
            "select": False,
            "a": True,
            "b": True,
        }
    }
    return render(request, "game/load_game.html", context)