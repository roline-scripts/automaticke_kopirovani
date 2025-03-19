import time
import keyboard
import pyperclip

import asyncio
from desktop_notifier import DesktopNotifier

from bin.DataManager import DataManager

# * Data processing
data = DataManager("input/")
data.processFiles()

# * Notifier
# notifier = DesktopNotifier()

# * Timer before start
countdown = 10
print(f"Script will start pasting in {countdown} seconds.")

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