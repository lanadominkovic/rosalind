# example 1
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"


"""Hamming distance between two strings of equal length is the number of positions at
which the corresponding symbols are different"""

def hamming_distance(s, t):
    if len(s) != len(t):
        print("Strings are not equal size!")
    else:
        hamming_dist = 0
        for position in range(len(s)): # len(s) == len(t) in this case
            if s[position] != t[position]:
                hamming_dist = hamming_dist + 1
        return hamming_dist

print(f"Hamming distance for this example is: {hamming_distance(s,t)}")