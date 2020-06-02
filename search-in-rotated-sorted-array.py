# https://leetcode.com/problems/search-in-rotated-sorted-array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand, i.e. [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array. Runtime complexity must be in the order of O(log n).
#
# Example: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


def find_rotation(a):
    '''
    Helper function, finds rotation index in a sorted and rotated array,
    Examples:
        find_rotation([4, 5, 6, 7, 0, 1, 2]) == 4
        find_rotation([1, 2, 3]) == 0
        find_rotation([2, 3, 4, 5, 1]) == 4
    '''
    i, j = 0, len(a) - 1
    while a[i] > a[j]:
        m = (i + j) // 2
        if a[m] > a[j]:
            i = m + 1
        else:
            j = m
    return i


assert find_rotation([4, 5, 6, 7, 0, 1, 2]) == 4
assert find_rotation([2, 4, 5, 6, 7, 0, 1]) == 5
assert find_rotation([6, 7, 0, 1, 2, 4, 5]) == 2
assert find_rotation([0, 1, 2, 4, 5, 6, 7]) == 0
assert find_rotation([7, 1, 2, 4, 5, 6, 0]) == 6


def bsearch(a, i, j, target):
    '''
    Helper function, basic binary search. Searches for target in array a bounded by [i, j] interval.
    Returns index of found target, or -1 if not found
    '''
    while i < j:
        m = (i + j) // 2
        if target > a[m]:
            i = m + 1
        else:
            j = m
    return i if a[i] == target else -1


def search0(a, target):
    '''
    Solution function. 2-3-pass binary search.
    '''
    # find rotation index, rotation index devides an array into two sorted parts:
    # [0, r - 1] and [r, n], where n is the last element's index
    r = find_rotation(a)

    # try to find a target in the [r, n] part
    found = bsearch(a, r, len(a) - 1, target)
    # found?
    if found >= 0:
        return found
    # r is the first element?
    if r == 0:
        # if so, [r, n] part represents whole array, and we didn't find a target
        return -1

    # try to find a target in the [0, r - 1] part
    return bsearch(a, 0, r - 1, target)


def search1(a, target):
    '''
    Solution function. 1-pass binary search.
    '''
    if not a:
        return -1
    # set initial search range: [0, len(a) - 1], i.e. whole array
    i, j = 0, len(a) - 1
    # search invariant: i < j, otherwise search ended.
    while i < j:
        # devide [i, j] range into two parts, left and right, [i, m] and [m + 1, j] respectively
        # m is a math avg of i and j boundaries
        m = (i + j) // 2
        # is left [i, m] part sorted?
        if a[i] < a[m]:
            # is target within the [i, m] range?
            if target >= a[i] and target <= a[m]:
                # search for target and return
                return bsearch(a, i, m, target)
            else:
                # target is not within the range
                # set next search boundaries to the right
                i = m + 1
        else:
            # no, left [i, m] part isn't sorted,
            # therefore, right [m + 1, j] part is sorted
            # is target within the [m + 1, j] range?
            if target >= a[m + 1] and target <= a[j]:
                # search for target and return
                return bsearch(a, m + 1, j, target)
            else:
                # target is not within the range
                # set next search boundaries to the left
                j = m
    return i if a[i] == target else -1


# Test


a = [4, 5, 6, 7, 0, 1, 2]
assert search0(a, 0) == search1(a, 0) == 4
assert search0(a, 3) == search1(a, 3) == -1

a = [2, 5]
assert search0(a, 2) == search1(a, 2) == 0
assert search0(a, 5) == search1(a, 5) == 1
assert search0(a, 1) == search1(a, 1) == -1
assert search0(a, 3) == search1(a, 3) == -1
assert search0(a, 6) == search1(a, 6) == -1
