# p36.py
# Problem P-1.36: Word counter.

class WordCounter:
    def __init__(self, text):
        self.text = text
        self.word_count = {}

    def count_words(self):
        words = self.text.split()
        for w in words:
            self.word_count[w] = self.word_count.get(w, 0) + 1

    def show_result(self):
        for w, c in self.word_count.items():
            print(w, ":", c)
