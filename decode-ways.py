# https://leetcode.com/problems/decode-ways

# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# A = 1
# B = 2
# ...
# Z = 26

# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Let's decode [1,2,1,2] step-by-step:

# 1. Take first digit, input = [1]. The only solution is: [1]
# 
# 2. Take second digit, input = [1,2]. Digit 2 maps on letter "B", so it can be attached on its own to the solutions of 
#    previous input = [1]: [1,2]. Moreover, digit 2 along with previous digit 1 forms number 12, which maps on letter "L",
#    so 12 can also be attached to the solutions of "previous previous" input (at this step it's empty).
# 
#    Therefore, the solutions for input [1,2] are: [1,2] and [12]
# 
# 3. Take third digit, input = [1,2,1]. Digit 1 maps on letter "A", so it can be attached on its own to the solutions of 
#    previous input = [1,2]: [1,2,1] [12,1]. Moreover, digit 1 along with previous digit 2 forms number 21, which maps on letter "U",
#    so 21 can also be attached to the solutions of "previous previous" input = [1]: [1,21].
# 
#    Therefore, the solutions for input [1,2,1] are: [1,2,1] [12,1] [1,21]
#
# 4. Take forth digit, input = [1,2,1,2]. Digit 2 maps on letter "B", so it can be attached on its own to the solutions of 
#    previous input = [1,2,1]: [1,2,1,2] [12,1,2] [1,21,2]. Moreover, digit 2 along with previous digit 1 forms number 12, 
#    which maps on letter "L", so 12 can also be attached to the solutions of "previous previous" input = [1,2]: [1,2,12] and [12,12].
# 
#    Therefore, the solutions for input [1,2,1,2] are: [1,2,1,2] [12,1,2] [1,21,2] [1,2,12] [12,12]
# 
# Given example above, it's clear that the problem exhibits optimal substructure property: solution to the main problem can be 
# constructed from solutions to its subproblems. Let's formulate optimal substructure of the problem:
# 
# Let f(i) be optimal solution for upto i-th digits. Let s[i] be i-th digit of given array.
# Then f(i) = |
#             | f(i - 1) + f(i - 2)   if s[i] > 0 and forms a valid 2-digit number with previous digit. I.e. if x = 10 * s[i-1] + s[i] is within [11, 26] range
#             | f(i - 1)              if s[i] > 0 but doesn't form a valid 2-digit number with previous digit.
#             | f(i - 2)              if s[i] == 0; (0 isn't mapped on any letter, it can only be attached to the previous digit to form a letter)
# 

from functools import lru_cache


def decode(s):

    # transform input string into int array
    s = list(map(int, s))

    # validate int array
    # 1. leading 0 is not acceptable
    if s[0] == 0:
        return 0

    # 2. any digit before 0 must be either 1 or 2
    for i in range(1, len(s)):
        if s[i] == 0 and not 0 < s[i - 1] < 3:
            return 0

    # Recursive function of Optimal Substructure
    @lru_cache(maxsize=None)
    def f(i):
        if i <= 0:
            return 1

        if s[i] == 0:
            return f(i - 2)

        res = f(i - 1)
        if s[i - 1] == 1 or (s[i - 1] == 2 and s[i] < 7):
            res += f(i - 2)

        return res

    return f(len(s) - 1)

# Test

assert decode("1212") == 5
assert decode("789") == 3
