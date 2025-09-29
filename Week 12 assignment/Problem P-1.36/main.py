# main36.py
from p36 import WordCounter

def main():
    wc = WordCounter("this is a test this is simple test")
    wc.count_words()
    wc.show_result()

if __name__ == "__main__":
    main()
