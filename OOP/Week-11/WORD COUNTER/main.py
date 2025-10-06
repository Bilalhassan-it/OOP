# main.py
# This file runs the program using the WordCounter class.

from word_counter import WordCounter   # import class from source file

# -------- Main Program --------
if __name__ == "__main__":
    # Take input from user
    text = input("Enter words separated by spaces: ")

    # Create object of WordCounter class
    counter = WordCounter(text)

    # Call methods of the class
    counter.count_words()
    counter.show_result()
