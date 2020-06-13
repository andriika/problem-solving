# https://leetcode.com/problems/maximal-square/

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Input:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4


def maxsquare(grid):
    '''
    Dynamic Programming Optimal Substructure:
    Let f(i,j) be the diagonal length of the square whose bottom right corner is at the (i,j) cell.
    Then f(i,j) can be defined recursively as:
         f(i,j) = 1 + min(f(i, j - 1), dp(i - 1, j - 1), dp(i - 1, j))
    '''
    # edge case return
    if not grid:
        return 0

    # n - row size
    n = len(grid[0])

    # transform input, so that all elements are ints
    rows = map(lambda row: list(map(int, row)), grid)

    # process 1st row
    row = next(rows)
    res = max(row)

    # process remaining rows
    for crow in rows:
        # crow - current row
        # process 1st element of the current row
        res = max(res, crow[0])
        # process remaining elements of the current row
        for j in range(1, n):
            if crow[j] > 0:
                # update current element according to the problem's optimal substructure definition
                crow[j] = 1 + min(crow[j - 1], row[j - 1], row[j])
                # update running max
                res = max(res, crow[j])

        # current row has been processed, update row
        row = crow

    return res * res

# Test


assert maxsquare([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]]
) == 4
