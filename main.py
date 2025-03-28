import time
import keyboard
import pyperclip
import sys
import os

import asyncio
# from desktop_notifier import DesktopNotifier

from src.DataManager import DataManager

# * Barevny text
class _bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class status_tag:
    FAIL = f"[ CHYBA ]"
    OK = f"[ OK ]"
    WARNING = f"[ POZOR ]"
    INFO = f"[ INFO ]"
    USERPROMPT = f"[ ? ]"

# * Upozorneni pred spustenim
print(f"DŮLEŽITÉ: Jakmile program začne vkládat SN do Logi, není možné počítač vzužívat k ničemu jinému. \nProgram pouze mačká tlačítka za vás, proto pokud začnete během jeho chodu mačkat další tlačítka, rozhodíte ho \na nebude tlačítka mačkat tak, jak by měl.\n")
input("Po přečtení zprávy stiskněte jakékoliv tlačíko.")
clear = lambda: os.system('cls')
clear()
time.sleep(0.2)

# * Data processing
print(f"{status_tag.INFO} Zpracovávám data...")
try:
    data = DataManager("input/")
    data.processFiles()
except:
    print(f"{status_tag.FAIL} Při zpracovávání dat došlo k chybě. Ukončuji program...")
    time.sleep(5)
    sys.exit()

if len(data.file_list) == 0:
    print(f"{status_tag.FAIL} Nebyly nalezeny žádné dokumenty ve složce input. Vložte do složky data a restartujte program.")
    input("Stiskněte jakékoliv tlačítko pro ukončení progragmu...")
    sys.exit()
if len(data.file_list) == 1:
    print(f"{status_tag.INFO} Nalezen 1 dokument. Zobrazuji zpracovaná data.", sep="\n")
elif len(data.file_list) < 10:
    print(f"{status_tag.INFO} Nalezeny {len(data.file_list)} dokumenty. Zobrazuji zpracovaná data.")
else:
    print(f"{status_tag.INFO} Nalezeno {len(data.file_list)} dokumentů. Pro kontrolu zpracovaná data.")

print(f"""\n\tDatum poslední úpravy složky input: {time.ctime(os.path.getmtime("input"))}
\tPočet SN v dokumentech / Počet načtených SN: {data.getAmountSum()} / {len(data.serial_nums)}
\tPrvní tři sériová čísla: {", ".join(data.serial_nums[:3])}
""")
print(f"{status_tag.INFO} Zkontrolujte prosím správnost uvedených informací.")
print(f"{status_tag.WARNING} Nezapomeňte, že zatímco program vkládá čísla do Logi, není možné na počítači dělat nic jiného")

while True:
    user_input = input(f"{status_tag.USERPROMPT} Chcete spustit program? (a/n) ")
    try:
        if user_input.lower() == "n" or user_input.lower() == "ne":
            print(f"{status_tag.INFO} Program ukončen uživatelem. Zavřete oči, odcházím!")
            time.sleep(5)
            sys.exit()
        elif user_input.lower() == "a" or user_input.lower() == "ano":
            break
        else:
            print(f"{status_tag.FAIL} Neplatný vstup. Zkuste to znovu.")
    except AttributeError:
        print(f"{status_tag.FAIL} Neplatný vstup. Zkuste to znovu.")

# * Notifier
# TODO Replace terminal message with desktop alert
# notifier = DesktopNotifier()

# * Timer before start
countdown = 10
print(f"{status_tag.INFO} Automatické vkládání čísel začne za {countdown} vteřin.")

def writeNums(nums: list):
    current_item = 1 # 
    total_len = len(nums)
    for num in data.serial_nums:
        time.sleep(0.2)
        keyboard.send("a")
        keyboard.send("ctrl+a")
        pyperclip.copy(f"{num}")
        keyboard.send("ctrl+v")
        time.sleep(1)
        keyboard.send("enter")
        time.sleep(0.1)
        keyboard.send("2")
        time.sleep(0.1)
        keyboard.send("enter")
        time.sleep(0.1)
        print(f"{status_tag.OK} Vloženo SN ({current_item}/{total_len}): {num}")
        current_item += 1
    pyperclip.copy("HOTOVO")
    keyboard.send("ctrl+v")

time.sleep(countdown)

writeNums(data.serial_nums)

input(f"\n{status_tag.OK} Vkládání dokončeno. Stiskněte jakoukolilv klávesu pro ukončení programu.")
