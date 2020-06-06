# https://leetcode.com/problems/invert-binary-tree/

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

from tree import TreeNode


def invert(root: TreeNode):

    # postorder dfs traversal, for each node, switch left and right children
    def dfs(node: TreeNode):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        node.left, node.right = node.right, node.left

    dfs(root)
    return root

# Test
