import re
import time
import keyboard
import pyperclip
import sys

from bin.DataManager import DataManager

# * Data processing
data = DataManager("input/")
data.processFiles()

