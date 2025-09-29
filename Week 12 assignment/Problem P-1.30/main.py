# main30.py
from p30 import DivisionCounter

def main():
    num = 100
    dc = DivisionCounter(num)
    print(f"{num} can be divided by 2 → {dc.count_divisions()} times")

if __name__ == "__main__":
    main()
