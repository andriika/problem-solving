# https://leetcode.com/problems/binary-search-tree-iterator/

# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
#   7
#  / \
# 3  15
#   /  \
#  9   20
# Example:

# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false

# Definition for a binary tree node.

from tree import TreeNode

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        root = node.right
        while root:
            self.stack.append(root)
            root = root.left
        return node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()