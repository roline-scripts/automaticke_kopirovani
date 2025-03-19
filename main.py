import time
import keyboard
import pyperclip

import asyncio
# from desktop_notifier import DesktopNotifier

from bin.DataManager import DataManager

# * Data processing
data = DataManager("input/")
data.processFiles()

# * Upozorneni pred spustenim
print("DŮLEŽITÉ: Jakmile program začne vkládat SN do Logi, není možné počítač vzužívat k ničemu jinému. \nProgram pouze mačká tlačítka za vás, proto pokud začnete během jeho chodu mačkat další tlačítka, rozhodíte ho \na nebude tlačítka mačkat tak, jak by měl.\n")
input("Stisknutím jakéhokoliv tlačítka zahájíte odpočet programu.")

# * Notifier
# TODO Replace terminal message with desktop alert
# notifier = DesktopNotifier()

# * Timer before start
countdown = 10
print(f"Vkládání čísel začne za {countdown} vteřin.")

def writeNums(nums: list):
    for num in data.serial_nums:
        print(num)
        pyperclip.copy(f"{num}")
        keyboard.send("ctrl+v")
        time.sleep(1)
        keyboard.send("enter")
        time.sleep(0.1)
        keyboard.send("2")
        time.sleep(0.1)
        keyboard.send("enter")
        time.sleep(0.1)
    pyperclip.copy("HOTOVO")
    keyboard.send("ctrl+v")

time.sleep(countdown)

writeNums(data.serial_nums)

input("Vkládání dokončeno. Stiskni jakoukolilv klávesu pro ukončení programu.")