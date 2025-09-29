# main33.py
from p33 import HandheldCalculator

def main():
    hc = HandheldCalculator()
    hc.calculate_and_store("10+20")
    hc.calculate_and_store("50/5")
    hc.calculate_and_store("7*8")
    hc.show_memory()

if __name__ == "__main__":
    main()
