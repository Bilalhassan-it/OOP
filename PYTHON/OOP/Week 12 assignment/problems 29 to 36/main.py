# main.py
from problems import (
    PermutationGenerator,
    DivisionCounter,
    ChangeMaker,
    SimpleCalculator,
    HandheldCalculator,
    SentenceWriter,
    BirthdayParadox,
    WordCounter
)

def main():
    print("=== P-1.29 ===")
    pg = PermutationGenerator(['a', 'b', 'c', 'd'])
    pg.generate_strings(2)

    print("\n=== P-1.30 ===")
    dc = DivisionCounter(100)
    print("Divisions:", dc.count_divisions())

    print("\n=== P-1.31 ===")
    cm = ChangeMaker([100, 50, 20, 10, 5, 1])
    print("Change for 270 given 500:", cm.make_change(270, 500))

    print("\n=== P-1.32 ===")
    sc = SimpleCalculator()
    print("3+5*2 =", sc.calculate("3+5*2"))

    print("\n=== P-1.33 ===")
    hc = HandheldCalculator()
    hc.calculate_and_store("10+20")
    hc.calculate_and_store("50/5")
    hc.show_memory()

    print("\n=== P-1.34 ===")
    sw = SentenceWriter()
    sw.write_sentence("I will never spam my friends again.", 5)

    print("\n=== P-1.35 ===")
    bp = BirthdayParadox(23)
    prob = bp.run_experiment(5000)
    print("Probability of shared birthday (23 people):", prob)

    print("\n=== P-1.36 ===")
    wc = WordCounter("this is a test this is simple")
    wc.count_words()
    wc.show_result()

if __name__ == "__main__":
    main()
