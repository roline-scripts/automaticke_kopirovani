import json
import os

class SettingsManager:
    def __init__(self):
        with open("settings.json") as file: 
            self.settings = json.load(file)

    def __str__(self):
        return str(self.settings)

if __name__ == "__main__":
    print(SettingsManager())