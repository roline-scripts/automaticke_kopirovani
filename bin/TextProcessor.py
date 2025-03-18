import re
import os

# * Modul DataManager zpracovává všechna data obsažena ve složce input, která je umístěna ve hlavní složce skriptu. Obsažená data jsou vyhodnocována pomocí regexu.
# * Nezáleží tedy na tom, zda jsou všechna naskenovaná čísla umístěna v jednom souboru, nebo jsou rozdělena do více souborů.

class DataManager():
    def __init__(self, file_name: str): # enter file name as it is in the default input folder
        self.DEFAULT_INPUT_DIR = "../input"
        self.FILE_PATH= self.DEFAULT_INPUT_DIR + "/" + file_name
        self.FILE = open(self.FILE_PATH, "r").read()

        self.file_list = os.listdir(self.DEFAULT_INPUT_DIR)
        
        # REGEX PATTERNS 
        self.SN_PATTERN = r"\d{17}\s\d{5}"   
        self.DELIVERY_ID_PATTERN = r"\d{18}"
        self.AMOUNT = r"(?<=;)\d{2}(?=;)"
        self.serial_nums = []
        self.delivery_id = []
        self.amount = []

    def processFile(self): 
        self.serial_nums = self.matchPattern(self.SN_PATTERN)
        self.delivery_id = self.matchPattern(self.DELIVERY_ID_PATTERN)
        self.amount = self.matchPattern(self.AMOUNT)

    def matchPattern(self, exp):
        found = re.findall(exp, self.FILE)
        return found

def main():
    test_path = "test1.txt"
    file = DataManager(test_path)
    print(file.file_list)
    file.processFile()
    for i in file.serial_nums:
        print(i)

if __name__ == "__main__":
    main()
