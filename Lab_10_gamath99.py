"""
Word count project 
Gama MATHURIN
The program is meant to analyze word frequency in one of four predefined text files selected by the user. 
July 5, 2026
"""
from pathlib import Path
import string

class WordAnalyzer:
    """initialize the filepath to store it as priate pathlibrary"""
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    """Create method to modify the text"""
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
"""Create the main function to excute the game"""
def main():
    files = {
        "1":Path("princess_mars.txt"),
        "2":Path("Tarzan.txt"),
        "3":Path("treasure_island.txt"),
        "4":Path("monte_cristo.txt")
    }

    choice = ""
    #Create the menu loop for selection
    while choice != "5":
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. Princess Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. Monte Cristo")
        print("5. Exit")

        #create a statement to validate the user input     
        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")


        elif choice in files:
            selected_file = files[choice]

            print(f"\nProcessing '{selected_file.name}'...\n")

            analyzer = WordAnalyzer(selected_file)

            if analyzer.process_file():
                analyzer.print_report()
            
            input("\nPress Enter to return to the menu...")

        else:
            print("\ninvalid choice. Please select from 1-5. ")
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()