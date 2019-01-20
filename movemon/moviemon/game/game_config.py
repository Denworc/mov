from random import randint

from django.conf import settings

import pickle


class GameConfig:

    def load(self, config):
        self.user_params = config
        f = open("user_params", "wb")
        pickle.dump(self.user_params, f)
        f.close()

    def dump(self):
        f = open("user_params", "rb")
        user_params = pickle.load(f)
        f.close()
        return user_params

    def get_random_movie(self):
        f = open("user_params", "rb")
        user_params = pickle.load(f)
        f.close()
        r = randint(0, 9)
        if user_params["films_get"][r]:
            while user_params["films_get"][r]:
                r = randint(0, 9)
        return r

    def load_default_settings(self):
        self.settings = settings.GAME_SETTINGS
        self.user_params = {
            "position": {
                "x": self.settings["start_x"],
                "y": self.settings["start_y"],
            },
            "chosen_l": {
                "load_one": False,
                "load_two": False,
                "load_three": False,
            },
            "films": {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: "",
                6: "",
                7: "",
                8: "",
                9: "",
            },
            "films_get": {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "",
                5: "",
                6: "",
                7: "",
                8: "",
                9: "",
            },
            "balls_count": 3,
            "bettle_monster": 11,
        }
        f = open("user_params", "wb")
        pickle.dump(self.user_params, f)
        f.close()

    def get_strength(self):
        f = open("user_params", "rb")
        user_params = pickle.load(f)
        res = 0
        for x in user_params["films_get"]:
            if x:
                res += 1
        f.close()
        return res

    def get_movie(self, n):
        f = open("user_params", "rb")
        user_params = pickle.load(f)
        return user_params["films"][int(n)]
