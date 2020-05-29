# https://leetcode.com/problems/3sum/

# Given an array integers, are there elements a, b, c such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# The solution set must not contain duplicate triplets.

# Example: nums = [-1, 0, 1, 2, -1, -4]
# Solution: [[-1, 0, 1],[-1, -1, 2]]


def sum3(a):
    res = set()  # result set
    useen = set()  # processed "u" values

    # for each (u, v) pair
    for i in range(len(a) - 1):
        u = a[i]

        # optimization:
        # have we gone through "u pairs" before?
        if u in useen:
            # no need to go through again
            continue

        vseen = set() # seen values (for current u cycle)
        for j in range(i + 1, len(a)):
            v = a[j]

            # for current (u, v) pair, find x, such that u + v + x = 0, i.e x = -u - v
            x = -u - v
            # x has seen in current u cycle?
            if x in vseen:
                # create sorted tuple of u, v and x values and add it to the result set
                res.add(asctuple3(u, v, x))

            # add current v value to the "seen set"
            vseen.add(v)
        # add current u value to the "seen set"
        useen.add(u)

    # transform result set to the required type: list[list[int]]
    res = list(map(lambda t: list(t), res))
    return res


# efficiently sorts 3 values in asc order and returns them in as a tuple
def asctuple3(a, b, c):
    if b < a:
        a, b = b, a
    if c < a:
        return c, a, b
    elif c > b:
        return a, b, c
    else:
        return a, c, b

# Test

assert sum3([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert sum3([0, 0, 0, 0, 0]) == [[0, 0, 0]]

# Follow up optimization: 
# Instead of re-creating vseen set on each u cycle, we can create vseen dictionary once, where key=v and value=u.
# Therefore, expression "x in vseen and vseen[v] == u" let us know if x value has seen in current u cycle or not
