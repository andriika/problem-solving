# https://leetcode.com/problems/validate-binary-search-tree/

# Given a binary tree, determine if it is a valid binary search tree. Assume a BST is defined as follows:
#    - The left subtree of a node contains only nodes with keys less than the node's key.
#    - The right subtree of a node contains only nodes with keys greater than the node's key.
#    - Both the left and right subtrees must also be binary search trees.
#
# Examples:
#
# Input: [2,1,3]
#    2
#   / \
#  1   3
#
# Output: true

# Input: [5,1,4,null,null,3,6]
#    5
#   / \
#  1   4
#     / \
#    3   6
#
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

from tree import TreeNode


def inorderIterator(node):
    '''
    Helper function. DFS in-order tree iterator. Given node is the tree's root
    '''
    stack = []
    # push whole left branch of the node to the stack
    while node:
        stack.append(node)
        node = node.left

    # for each node in the stack
    while stack:

        # pop and yield head of the stack
        node = stack.pop()
        yield node.val

        # node has been processed (yielded)
        # get right child of the processed node
        node = node.right
        # push whole left branch of the right child to the stack
        while node:
            stack.append(node)
            node = node.left


def isvalid(root):
    pv = -float('inf') # value of previous node
    # iterate tree in-order and make sure every node is greater then previous one
    for v in inorderIterator(root):
        if not v > pv:
            # found non ascending node, given tree is not a BST
            return False
        pv = v
    # all nodes are in asc order, given tree is a valid BST
    return True

# Test


assert isvalid(TreeNode.create([2, 1, 3]))
assert not isvalid(TreeNode.create([1, 1]))
assert not isvalid(TreeNode.create([5, 1, 4, None, None, 3, 6]))
