# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Idea:
# This problem exhibits an optimal substructure: Let f(i) be the largest sum subarray that ends on i-th element.
# Then f(i) = max(f(i-1) + a[i], a[i]), where a[i] is i-th number in an input array
# Using this formula, we can calculate result for each i-th element and pick max one

def maxsub0(a):

    def f(i, callback):
        if i < 0:
            return 0
        res = max(f(i - 1, callback) + a[i], a[i])
        callback(res)
        return res

    res = a[0]

    def updateRes(v):
        nonlocal res
        res = max(res, v)

    f(len(a) - 1, updateRes)
    return res

# Iterative version:


def maxsub1(a):
    maxres = ires = a[0]
    for i in range(1, len(a)):
        ires = max(ires + a[i], a[i])
        maxres = max(maxres, ires)
    return maxres

# Test


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

assert maxsub0(a) == maxsub1(a) == 6
