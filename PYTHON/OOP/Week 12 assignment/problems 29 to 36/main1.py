def p29():
    # P-1.29: Print all possible strings using 'c', 'a', 't', 'd', 'o', 'g' exactly once
    chars = ['c', 'a', 't', 'd', 'o', 'g']

    def permute(s, l, r):
        if l == r:
            print("".join(s))
        else:
            for i in range(l, r + 1):
                s[l], s[i] = s[i], s[l]
                permute(s, l + 1, r)
                s[l], s[i] = s[i], s[l]   # backtrack

    permute(chars, 0, len(chars) - 1)