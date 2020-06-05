# https://leetcode.com/problems/next-permutation/

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


def reverse(a, i, j):
    '''
    Helper. Reverses in-place [i, j] range of the given array
    '''
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


def nextperm(a):

    # edge cases
    if not a or len(a) == 1:
        return

    # go backwards over numbers and find first descending number
    # i.e. when going backwards, i-th is a descending number if a[i] < a[i + 1]
    for i in range(len(a) - 2, -1, -1):
        if a[i] < a[i + 1]:
            # found, i-th number is a descending one
            # now we need to switch i-th and j-th numbers, such that j belongs to [i+1, len(a)) range and
            # a[j] is the smallest number in the range that is larger then a[i]
            # find j
            for j in range(len(a) - 1, i, -1):
                if a[j] > a[i]:
                    # j found, swith i and j
                    a[i], a[j] = a[j], a[i]
                    # and reverse [i + 1, len(a)) range
                    reverse(a, i + 1, len(a) - 1)
                    return
            return

    # descending number not found, just reverse whole input array
    reverse(a, 0, len(a) - 1)

# Test


a = [1, 2, 3]
nextperm(a)
assert a == [1, 3, 2]

a = [2, 2, 0, 4, 3, 1]
nextperm(a)
assert a == [2, 2, 1, 0, 3, 4]

a = [1, 3, 2]
nextperm(a)
assert a == [2, 1, 3]

a = [3, 2, 1]
nextperm(a)
assert a == [1, 2, 3]

a = [1, 1, 5]
nextperm(a)
assert a == [1, 5, 1]

a = [1, 2, 0]
nextperm(a)
assert a == [2, 0, 1]
