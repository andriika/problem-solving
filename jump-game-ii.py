# https://leetcode.com/problems/jump-game-ii

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Example:
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

from functools import lru_cache

# Optimal Substructure Definition 1:
# 
# Let f(n) be a minimum jumps to reach n-th element in given array. Then f(n) defined as:
# f(n) =
#       | 0 if n = 0, i.e. first element
#       | min([f(i)..]) + 1 where "i" is a set of indexes in [0, n) range and such that the n-th index is reacheable from it (i.e. i + a[i] >= n)

# Runtime O(n^2)


def jump0(a):

    def f(n):
        if n == 0:
            return 0
        r = float('inf')
        for i in range(0, n):
            if i + a[i] >= n:
                r = min(r, f(i))
        return r + 1
    return f(len(a) - 1)

# Optimal Substructure Definition 2: (Go Backwards)
# 
# Let f(n) be a minimum jumps to reach the last element from n-th. Then f(n) defined as:
# f(n) =
#       | 0 if n is the last index
#       | min([f(i)..]) + 1 where i is [n + 1, n + a[n]] range, i.e. all elements that are reachable from i-th element

# Runtime: Still O(n^2), but slightly faster on practice than jump0


def jump1(a):

    def f(n):
        if n == len(a) - 1:
            return 0
        r = float('inf')
        for i in range(n + 1, min(n + a[n] + 1, len(a))):
            r = min(r, f(i))
        return r + 1
    return f(0)

# Iterative bottom-up version of jump1. Still O(n^2)


def jump2(a):
    res = [0] * len(a)
    res[-1] = 0
    for n in range(len(a) - 2, -1, -1):
        r = float('inf')
        for i in range(n + 1, min(n + a[n] + 1, len(a))):
            r = min(r, res[i])
        res[n] = r + 1
    return res[0]


# Greedy approach O(n). Explanation of greedy steps for the [2, 3, 1, 1, 4] input:
#
# 1. Let global Max Jump Length (MJL) be MJL of the first element. MJL formula for the i-th element is: f(i) = i + a[i] + 1. Therefore, f(0) = 0 + 2 + 1 = 3
# 2. Run cycle 1 for [1, 3) range, where 3 is the current global MJL.
#       a) Find max MJL among current cycle's elements. Found at index 1: 1 + a[1] + 1 = 1 + 3 + 1 = 5
#       b) Update global MJL with the new MJL found for the cycle (5 now)
# 3. Run cycle 2 for [3, 5) range, where 5 is the current global MJL.
#       a) MJL found at index 4
#       b) Update global MJL
# 4. All input elements are processed. Return number processed cycles (jumps) = 2

def jump3(a):

    # c - cycle (or jumps) counter
    # it also represent the result - minimum number of jumps to reach the last element
    c = 0

    j = min(0 + a[0] + 1, len(a))  # max jump length

    i = 1
    while i < len(a):
        # run cycle
        # find max jump index for the [i, j) range
        maxj = 0
        for k in range(i, j):
            maxj = max(maxj, k + a[k] + 1)

        # cycle ended
        # update i and j for the next cycle
        i = j
        j = min(maxj, len(a))

        # increment cycle counter
        c += 1

    return c


# Test

a = [5]
assert jump0(a) == jump1(a) == jump2(a) == jump3(a) == 0

a = [2, 3, 1, 1, 4]
assert jump0(a) == jump1(a) == jump2(a) == jump3(a) == 2

a = [2, 4, 1, 1, 4]
assert jump0(a) == jump1(a) == jump2(a) == jump3(a) == 2
