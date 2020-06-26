# https://leetcode.com/problems/01-matrix/

# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell. The distance between two adjacent cells is 1.

# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]


# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]


import collections

# Idea: BFS. Init BFS queue with all the 0 cells. Go over queue, for each cell in a queue check what distance current
# cell offers to its neigbors. If offered distance is less then current, update neigbor's distance in result matrix and push
# neighbor cell to the queue.


def distto0(matrix):

    # given m x n matrix
    m, n = len(matrix), len(matrix[0])

    # result matrix, initally all 0
    res = [[0] * n for _ in range(m)]

    # bfs queue
    q = collections.deque()

    # go over cells
    for i in range(m):
        for j in range(n):
            if matrix[i][j] > 0:
                # update result for non 0 cells to the biggest number
                res[i][j] = float('inf')
            else:
                # put 0 cells in the bfs queue
                q.append((i, j))

    # right, left, up and down directions
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # run bfs
    while q:
        i, j = q.popleft()

        # d is a potential distance of the neigbor cells
        # i.e. if current cell distance is x, then current cell can offer d = x + 1 distance to its neighbors
        d = res[i][j] + 1

        for di, dj in dirs:
            # coordinates of the neighbor cell
            i1, j1 = i + di, j + dj
            # if neighbor's coordinates are valid (in range) and
            # neighbor's current distance is bigger then potentail distance
            if 0 <= i1 < m and 0 <= j1 < n and res[i1][j1] > d:
                # update neighbor's distance
                res[i1][j1] = d
                # push to bfs queue for further processing
                q.append((i1, j1))
    return res


# Test

assert distto0([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
    [0, 0, 0], [0, 1, 0], [0, 0, 0]]


input = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [
    0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]

output = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [
    0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 2, 1, 1, 0, 1], [2, 1, 1, 1, 1, 2, 1, 0, 1, 0], [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]

assert distto0(input) == output
