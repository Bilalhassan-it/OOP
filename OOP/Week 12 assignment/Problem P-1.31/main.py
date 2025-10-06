# main31.py
from p31 import ChangeMaker

def main():
    cm = ChangeMaker([100, 50, 20, 10, 5, 1])
    print("Change for 270 given 500:")
    print(cm.make_change(270, 500))

if __name__ == "__main__":
    main()
