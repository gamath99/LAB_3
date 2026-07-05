"""
Word count project 
Gama MATHURIN
The program is meant to analyze word frequency in one of four predefined text files selected by the user. 
July 5, 2026
"""
from pathlib import Path
import string

class Wordanalyzer:
    def __int__(self, filepath):
        self.filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            punctuation_table = str.maketrans("", "", string.punctuation)

            with self.__filepath.open("r", encoding ="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(punctuation_table)
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True
        except FileNotFoundError:
            print(f"Error: The file '{self.__filepath}' was not found.")
            return False
        
    def print_report(self):
        words = sorted(self.__frequencies.keys())

        for word in words: 
            print(f"{word:<15}::{self.__frequencies[word]}")




