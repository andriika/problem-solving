# https://leetcode.com/problems/number-of-islands/

# Given a 2d grid map of 1 (land) and 0 (water), count the number of islands. Example:

# 11110
# 11010
# 11000
# 00000

# Output: 1

# 11000
# 11000
# 00100
# 00011

# Output: 3


def islands(grid):
    # m x n grid
    m, n = len(grid), len(grid[0])
    
    # keeps track of visited cells,
    # initialilized with all 0, as initially no cells are visted
    visited = []
    for _ in range(m):
        visited.append([0] * n)

    def visit(i, j):
        '''
        Helper function that visits whole land (island) from the given i, j starting cell.
        Updates visited array according to visted land cells. DFS recursion.
        '''
        if i < 0 or j < 0 or i == m or j == n or visited[i][j] or grid[i][j] == '0':
            return
        visited[i][j] = 1
        visit(i + 1, j)
        visit(i - 1, j)
        visit(i, j + 1)
        visit(i, j - 1)

    res = 0  # visit counter (result)
    for i in range(m):
        for j in range(n):
            # does i,j cell represent not visited land?
            if not visited[i][j] and grid[i][j] == '1':
                # visit land (island) and increment visit counter
                visit(i, j)
                res += 1

    return res


# Test


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

assert islands(grid) == 3
