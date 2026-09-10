# main32.py
from p32 import SimpleCalculator

def main():
    sc = SimpleCalculator()
    print("3 + 5 * 2 =", sc.calculate("3+5*2"))
    print("12 / 4 + 1 =", sc.calculate("12/4+1"))

if __name__ == "__main__":
    main()
