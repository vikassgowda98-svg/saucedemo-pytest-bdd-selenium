import json
from pathlib import Path


class ConfigReader:

    @staticmethod
    def load():

        path = (Path(__file__).parent.parent/ "config"/ "config.json")

        with open(path, "r") as file:
            return json.load(file)