# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

# Optimal Substructure:

# Define the function LCS(X, Y) as the longest common subsequence to X and Y. That function has 2 interesting properties:
#   1.  Suppose that two sequences both end in the same element. Then their LCS is the LCS of the sequence with 
#       the last element excluded, with the common last element appended.
#   2.  Suppose that the two sequences X and Y do not end in the same symbol. Then the LCS of X and Y is the longer 
#       of LCS(Xn,Ym-1) and LCS(Xn-1,Ym).

# That is, LSC function can be recursively defined as:
# f(i, j) =
#           []                              if i < 0 or j < 0
#           f(i - 1, j - 1) + x[i]          if x[i] == y[j]
#           max(f(i - 1, j), f(i, j - 1)))  if x[i] != y[i]


def lcs(x, y):
    def f(i, j):
        if i < 0 or j < 0:
            return []
        if x[i] == y[j]:
            r = f(i - 1, j - 1)[:]
            r.append(x[i])
            return r
        return max(f(i - 1, j), f(i, j - 1), key=lambda el: len(el))
    return f(len(x) - 1, len(y) - 1)


assert lcs("ABCD", "ACBAD") == list("ABD")
