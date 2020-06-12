# Given an array of integers and an integer k, you need to find the total number of
# continuous subarrays whose sum equals to k.

# Input:nums = [1,1,1], k = 2
# Output: 2

from collections import defaultdict


def sumk(a, k):

    # result: total number of subarrays whose sum = k
    res = 0

    # running cumulative sum of array's numbers
    csi = 0

    # memory, keeps seen cumulative sums along with total number of occurrences
    mem = defaultdict(lambda: 0)
    mem[0] = 1

    # Let sum(i, j) be a sum of numbers in [i, j] range. Let csum(i) = sum(0, i), i.e. csum(i) is a cumulative sum of upto i-th number
    # The idea is: If csum(i) == csum(j), then sum(i, j - 1) = 0.
    # For example: numbers = [1, 1, -1, 1]; csum(1) = csum(3) = 2, so sum(1, 2) should be 0: sum([1, -1]) == 0

    # The idea can be generalized: If csum(i) - csum(j) == k, then sum(i, j - 1) = k.

    # for each cumulative sum of the input array
    for i in range(len(a)):
        # add i-th number to the Si
        csi += a[i]

        # did we ever saw cumulative sum Sj, such that Sj = Si - k?
        if csi - k in mem:
            # number of times we saw Sj so far
            times = mem[csi - k]
            # add to resulting total
            res += times

        # add current Si along with number of occurrences to the "seen" memory
        mem[csi] += 1
    return res


# Test

assert sumk([1, 1, 1], 2) == 2
