# p29.py
# Problem P-1.29: Generate all possible strings of length n from given characters.

class PermutationGenerator:
    def __init__(self, characters):
        self.characters = characters   # store given characters

    def generate_strings(self, n, prefix=""):
        """Recursively generate all strings of length n."""
        if n == 0:
            print(prefix)
        else:
            for ch in self.characters:
                self.generate_strings(n - 1, prefix + ch)
