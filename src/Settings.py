import json
import keyboard

from utils import status_tag

class SettingsManager:
    def __init__(self, settings_path: str):
        self.SETTINGS_PATH = settings_path

        self.SUPPORTED_SETTINGS = {
            "unit_count": {
                "description": "Počet jednotek na jedné paletě (tj. počet SN na jednom listě).",
                "default_value": 32,
                "value_type": int
                },
            "reference_number": {
                "description": "Česká reference produktu, jehož SN chcete vkládat.",
                "default_value": "2",
                "value_type": str
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
        print()
        setting_count = 1
        for setting in self.SETTINGS:
            print(f"\t[{setting_count}] '{setting}' : {self.SETTINGS[setting]}")
            setting_count += 1
    
    def writeSetting(self):
        self.showActiveSettings()
        while True:
            id = input(f"{status_tag.USERPROMPT} Zadejte číslo nastavení, které chcete změnit. (zadejte _cancel pro zrušení) ")
            if id.lower() == "_cancel":
                print(f"{status_tag.INFO} Příkaz k úpravě předčasně ukončen. Nebyly provedeny žádné změny.")
                return 
            try:
                if int(id) <= 0:
                    raise IndexError
                name = list(self.SETTINGS.keys())[int(id)-1]
                break
            except ValueError:
                print(f"{status_tag.FAIL} Zadali jste neplatnou hodnotu. Zkuste to znovu.")
            except IndexError:
                print(f"{status_tag.FAIL} Vámi zadané číslo neexistuje.")
        new_value = input(f"{status_tag.USERPROMPT} Zadejte novou hodnotu pro nastavení '{name}'. ") # TODO Make func that checks new_value data type
        if name in self.SETTINGS.keys():
            self.SETTINGS[name] = new_value
            self.rewriteFile()
            print(f"{status_tag.OK} Nastavení '{name}' změněno na {new_value}")
        else:
            if name in self.SUPPORTED_SETTINGS.keys():
                self.SETTINGS[name] = new_value
                self.rewriteFile()
                print(f"{status_tag.OK} Nastavení '{name}' změněno na {new_value} a bylo automaticky aktivováno.")
            else:
                print(f"{status_tag.FAIL} Nastavení se jménem '{name}' neexistuje.")
    
    def explain(self, info_prompt=True):
        if info_prompt:
            print(f"{status_tag.INFO} Zobrazuji podporovaná nastavení a jejich vysvětlení:\n")
        setting_count = 1
        for setting in self.SETTINGS.keys():
            print(f"\t[{setting_count}] {setting}: {self.SUPPORTED_SETTINGS[setting]["description"]}")
            setting_count += 1

def settings_dialog(manager: SettingsManager):
    command_map = {
        "l": manager.explain,
        "e": manager.writeSetting,
        "v": manager.showActiveSettings,
        "q": "exit"
    }
    while True:
        print(f"""{status_tag.INFO} K dispozici jsou následující akce:
        \n\tl: zobrazit vysvětlení všech nastavení
        v: zobrazit hodnoty nastavení
        e: upravit nastavení
        q: opustit menu a spustit program""")
        user_input = input(f"\n{status_tag.USERPROMPT} Jakou akci chcete provést? ").lower()
        if user_input not in command_map:
            print(f"{status_tag.FAIL} Neplatná možnost. Zkuste to znovu.")
        elif user_input == "q":
            break
        else:
            command_map[user_input]()
            print()

if __name__ == "__main__":
    manager = SettingsManager("./src/settings.json")
    settings_dialog(manager)