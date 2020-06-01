# https://leetcode.com/problems/jump-game/

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.

# Examples:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

from functools import lru_cache

# Recursive top-down with memoization 0(n^2)

def jump0(a):

    k = len(a) - 1  # index of the last element

    # Calculates if i-th element of array "a" is a good one.
    # Any element is a good one, if it's possible to jump to the last element from it
    @lru_cache(maxsize=None)
    def f(i):
        # is i-th element is the last one (or beyond)?
        if i >= k:
            # last element is the target, so it's good anyway
            return True

        t = i + a[i]
        for j in range(t, i, -1):
            if f(j):
                return True
        return False

    # is the first element good one?
    return f(0)

# DP iterative bottom-up 0(n^2)

def jump1(a):
    k = len(a) - 1  # index of the last element
    r = [False] * len(a) # result array, keeps statuses of "a" array elements (good=True, bad=False)
    r[k] = True # last element is the target, so it's good anyway

    # go backwards over each element, and determine its status: good or bad
    for i in range(k - 1, -1, -1):
        # t - furthest index we can jump to
        t = i + a[i]
        # can we jump over the last element?
        if t > k:
            # i-th is good
            r[i] = True
            continue

        for j in range(t, i, -1):
            if r[j]:
                r[i] = True
                break

    return r[0]

# DP iterative bottom-up optimized 0(n) (or could we say greedy?)
# Get rid of inner "for j" (see jump1), by saving index of the last spotted good element  

def jump(a):
        k = len(a) - 1  # index of the last element
        r = [False] * len(a) # result array, keeps statuses of "a" array elements (good=True, bad=False)
        r[k] = True # the last element is the target, so it's good anyway
        ig = k # index of the last spotted good element

        # go backwards over each element, and determine its status: good or bad 
        for i in range(k - 1, -1, -1):
            # t - furthest index we can jump to
            t = i + a[i]
            # can we jump to the last spotted good element?
            if t >= ig:
                # we can, so i-th element is a good one too
                r[i] = True
                # also, it's the last spotted good element now
                ig = i
        
        # return status of the first element
        return r[0]

# Test


assert jump([2, 3, 1, 1, 4]) == True
assert jump([3, 2, 1, 0, 4]) == False
