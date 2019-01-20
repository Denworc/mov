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
        pass

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
            }
        }
        f = open("user_params", "wb")
        pickle.dump(self.user_params, f)
        f.close()

    def get_strength(self):
        pass

    def get_movie(self):
        pass
