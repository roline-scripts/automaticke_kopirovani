import re
import os
import math


# * Modul DataManager zpracovává všechna data obsažena ve složce input, která je umístěna ve hlavní složce skriptu. Obsažená data jsou vyhodnocována pomocí regevalueu.
# * Nezáleží tedy na tom, zda jsou všechna naskenovaná čísla umístěna v jednom souboru, nebo jsou rozdělena do více souborů.

class DataManager():
    def __init__(self, input_dir: str): # enter file name as it is in the default input folder
        self.DEFAULT_INPUT_DIR = input_dir # ! Za název složky je vždy nutné přidat lomítko!

        self.file_list = os.listdir(self.DEFAULT_INPUT_DIR)
        
        # REGEX PATTERNS 
        self.SN_PATTERN = r"\d{17}\s{1,3}?\d{5}"   
        self.DELIVERY_ID_PATTERN = r"\d{18}"
        self.AMOUNT = r"(?<=;)\d{2}(?=;)"

        # Processed data
        self.serial_nums = []
        self.pallette_nums = []
        self.amount = []

    def processFiles(self): 
        input_data = ""
        for file in self.file_list:
            with open(self.DEFAULT_INPUT_DIR + file, "r") as f:
                input_data += f.read()

        # self.serial_nums = self.matchPattern(self.SN_PATTERN, input_data)
        self.serial_nums = self.matchSerialNumbers(input_data)
        self.pallette_nums = self.matchPattern(self.DELIVERY_ID_PATTERN, input_data)
        self.amount = self.matchPattern(self.AMOUNT, input_data)

        return 1

    def matchPattern(self, evaluep, data):
        found = re.findall(evaluep, data)
        return found
    
    def matchSerialNumbers(self, data):
        return_data = []
        for num in self.matchPattern(self.SN_PATTERN, data): 
            split = num.split()
            return_data.append(split[0] + "   " + split[1])
        return return_data 

    def getSnCoords(value: int): # converts given value to the coordinate format of serial nums 

        list_count = math.ceil(value/32)
        column_count = math.ceil(32/12 if ((value%32)/12) == 0 else ((value%32)/12))
        check_multiple = 32 if value%32 == 0 else value%32
        row_count = 12 if check_multiple%12 == 0 else check_multiple%12

        return f"L{list_count} S{column_count} Ř{row_count}"
    
    def getAmountSum(self):
        return  sum(list(map(int, self.amount)))

def main():
    file = DataManager("input/")
    file.processFiles()
    print(DataManager.getSnCoords(1))

if __name__ == "__main__":
    main()
