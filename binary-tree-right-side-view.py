# https://leetcode.com/problems/binary-tree-right-side-view/

# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Example: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1        <-
#  /   \
# 2     3     <-
#  \     \
#   5     4   <-


from tree import TreeNode
from collections import deque


def rightside(root):
    # edge case
    if not root:
        return []

    res = []
    # traverse tree breadth-first and level-by-level using standard queue based approach
    # init queue with nodes of the first level, i.e. just the root node
    q = deque([root])
    n = len(q)  # keeps track of the current level lenght
    while q:
        # process all nodes of the current level (of size n)
        nn = 0  # length of the next level
        prevnode = None
        for _ in range(n):
            node = q.popleft()
            # child node exists?
            if node.left:
                # contribute child to the next level
                q.append(node.left)
                nn += 1
            # child node exists?
            if node.right:
                # contribute child to the next level
                q.append(node.right)
                nn += 1
            # node has been processed, update previous node
            prevnode = node

        # at the end of the cycle above, prevnode holds the last node of the current level,
        # which is also the right most, so add it to the result
        res.append(prevnode.val)
        # update level length
        n = nn

    return res

# Test


assert rightside(TreeNode.create([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
