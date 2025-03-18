import re
import os

# * Modul DataManager zpracovává všechna data obsažena ve složce input, která je umístěna ve hlavní složce skriptu. Obsažená data jsou vyhodnocována pomocí regexu.
# * Nezáleží tedy na tom, zda jsou všechna naskenovaná čísla umístěna v jednom souboru, nebo jsou rozdělena do více souborů.

class DataManager():
    def __init__(self): # enter file name as it is in the default input folder
        self.DEFAULT_INPUT_DIR = "../input/" # ! Za název složky je vždy nutné přidat lomítko!

        self.file_list = os.listdir(self.DEFAULT_INPUT_DIR)
        
        # REGEX PATTERNS 
        self.SN_PATTERN = r"\d{17}\s\d{5}"   
        self.DELIVERY_ID_PATTERN = r"\d{18}"
        self.AMOUNT = r"(?<=;)\d{2}(?=;)"

        # Processed data
        self.serial_nums = []
        self.delivery_id = []
        self.amount = []

    def processFiles(self): 
        input_data = ""
        for file in self.file_list:
            with open(self.DEFAULT_INPUT_DIR + file, "r") as f:
                input_data += f.read()

        self.serial_nums = self.matchPattern(self.SN_PATTERN, input_data)
        self.delivery_id = self.matchPattern(self.DELIVERY_ID_PATTERN, input_data)
        self.amount = self.matchPattern(self.AMOUNT, input_data)

    def matchPattern(self, exp, data):
        found = re.findall(exp, data)
        return found

def main():
    test_path = "test1.txt"
    file = DataManager()
    print(file.serial_nums)
    file.processFiles()
    for i in file.serial_nums:
        print(i)

if __name__ == "__main__":
    main()
