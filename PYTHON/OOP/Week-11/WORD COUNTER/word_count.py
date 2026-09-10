# word_counter.py
# This file contains the WordCounter class definition.
#from collections import Counter
class WordCounter:
    # Constructor (runs when we create an object)
    def __init__(self, text):
        self.text = text
        self.word_count = Counter()   # Use a Counter for efficiency

    # Method to count words
    def count_words(self):
        # Find all word sequences, converting to lowercase. This handles punctuation.
        words = re.findall(r'\b\w+\b', self.text.lower())
        self.word_count.update(words) # Efficiently count words

    # Method to show results
    def show_result(self):
        print("\nWord Frequency:")
        # Sort by word for consistent and readable output
        for word, count in sorted(self.word_count.items()):
            print(f"{word} : {count}")
