# https://leetcode.com/problems/diameter-of-binary-tree/

# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# Given a binary tree
#
#          1
#         / \
#        2   3
#       / \
#      4   5

# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

from tree import TreeNode


def diameter(node: TreeNode):

    # running maximum of diameters
    res = 0

    # DFS postorder traversal. Returns max depth of the node.
    # As side-effect, computes
    def depth(node: TreeNode, cb):
        nonlocal res
        # base case
        if not node:
            # depth of a node beyond leaf node is -1 (so depth of the leaf node is 0)
            return -1

        # get max depth of children
        l, r = depth(node.left, cb), depth(node.right, cb)
        # expose children depth via callback
        cb(l, r)
        # return max depth of the current node
        return max(l, r) + 1

    # running maximum of diameters
    res = 0

    # callback function that calculates diameter of the node based on 
    # their children depth and updates running maximum of diameters
    def onDepth(l, r):
        nonlocal res
        diameter = l + r + 2
        res = max(res, diameter)

    depth(node, onDepth)
    return res

# Test


assert diameter(TreeNode.create([1, 2, 3, 4, 5])) == 3
