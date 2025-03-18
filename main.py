import re
import time
import keyboard
import pyperclip
import sys

from bin.TextProcessor import DataManager

# * Data processing
data = DataManager("input/")
data.processFiles()

