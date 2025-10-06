# main29.py
from p29 import PermutationGenerator

def main():
    chars = ['a', 'b', 'c', 'd']
    pg = PermutationGenerator(chars)
    print("All strings of length 2:")
    pg.generate_strings(2)

if __name__ == "__main__":
    main()


