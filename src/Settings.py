import json

from utils import status_tag

class SettingsManager:
    def __init__(self, settings_path: str):
        self.SETTINGS_PATH = settings_path

        self.SUPPORTED_SETTINGS = {
            "unit_count": {
                "description": "Počet jednotek na jedné paletě (tj. počet SN na jednom listě).",
                "default_value": 32
                },
            "reference_number": {
                "description": "Česká reference produktu, jehož SN chcete vkládat.",
                "default_value": "2"
                }
        }

        with open(settings_path) as file: 
            self.loaded_json = json.load(file)
            settings = {}
            for setting in self.SUPPORTED_SETTINGS.keys():
                try:
                    settings[setting] = self.loaded_json[setting]
                except KeyError:
                    default_value = self.SUPPORTED_SETTINGS[setting]["default_value"]
                    print(f"{status_tag.FAIL} Nastavení pro '{setting}' nebylo nalezeno. Používám přednastavenou hodnotu: {default_value}")
                    settings[setting] = default_value
            self.SETTINGS = settings
        
        self.rewriteFile()

    def __str__(self):
        return str(self.SETTINGS)
    
    def rewriteFile(self):
        with open(self.SETTINGS_PATH, "w") as file:
            json.dump(self.SETTINGS, file, indent=True)
    
    def showActiveSettings(self):
        setting_count = 1
        for setting in self.SETTINGS:
            print(f"\t[{setting_count}] '{setting}' : {self.SETTINGS[setting]}")
            setting_count += 1
    
    def writeSetting(self, name: str, new_value):
        if name in self.SETTINGS.keys():
            self.SETTINGS[name] = new_value
            self.rewriteFile()
            print(f"{status_tag.INFO} Nastavení '{name}' změněno na {new_value}")
        else:
            if name in self.SUPPORTED_SETTINGS.keys():
                self.SETTINGS[name] = new_value
                self.rewriteFile()
                print(f"{status_tag.INFO} Nastavení '{name}' změněno na {new_value} a bylo automaticky aktivováno.")
            else:
                print(f"{status_tag.CHYBA} Nastavení se jménem '{name}' neexistuje.")
    
    def explain(self):
        print(f"{status_tag.INFO} Zobrazuji podporovaná nastavení a jejich vysvětlení:\n")
        unknown_settings = []
        for setting in self.SETTINGS.keys():
            if setting in self.SUPPORTED_SETTINGS.keys():
                print(f"\t{setting}: {self.SUPPORTED_SETTINGS[setting]["description"]}")
            else:
                unknown_settings.append(setting)
        if unknown_settings:
            print(f"\n\tNeznámá nastavení: {", ".join(unknown_settings)}")

if __name__ == "__main__":
    manager = SettingsManager("./src/settings.json")
    manager.showActiveSettings()
    manager.explain()