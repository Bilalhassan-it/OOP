"""                                     R-1.8 Solution

Q: If string s has length n, and index k is negative (-n ≤ k < 0), what is the equivalent positive index j?
Concept:

Python mein negative index ka matlab hai  """
#j = n + k

# s = "BILAL"
# n = len(s)    # length = 6

# k = -2
# print("s[k] =", s[k])     # negative index
# j = n + k
# print("s[j] =", s[j])     # equivalent positive index
# Example string
""".................................................................................................................."""
s = "BILAL"
n = len(s)   # length of string is 5

#pythinic way
for k in range(-n, 0):   # k goes from -5 to -1
    print("s[", k, "] =", s[k], "  |  s[", n+k, "] =", s[n+k])