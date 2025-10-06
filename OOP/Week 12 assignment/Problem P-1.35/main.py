# main35.py
from p35 import BirthdayParadox

def main():
    bp = BirthdayParadox(23)
    prob = bp.run_experiment(5000)
    print("Probability of shared birthday (23 people):", prob)

if __name__ == "__main__":
    main()
