# p34.py
# Problem P-1.34: Write a sentence multiple times.

class SentenceWriter:
    def write_sentence(self, sentence, times=100):
        for i in range(times):
            print(f"{i+1}: {sentence}")
