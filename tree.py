import collections

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'(val={self.val})'

    @classmethod
    def create(cls, nodes):
        root = cls(nodes[0])
        q = collections.deque()
        q.append(root)
        i = -1
        while q:
            node = q.popleft()
            i += 1

            l = 2 * i + 1
            if l >= len(nodes):
                continue

            if node and nodes[l] is not None:
                left = cls(nodes[l])
                node.left = left
            else:
                left = None
            q.append(left)

            r = l + 1
            if r >= len(nodes):
                continue

            if node and nodes[r] is not None:
                right = cls(nodes[r])
                node.right = right
            else:
                right = None
            q.append(right)

        return root


def bfsIterator(node):
    q = collections.deque()
    q.append(node)
    while q:
        node = q.popleft()
        yield node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)



def inorderIterator(node):
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


if __name__ == "__main__":
    tree = [10, 5, 15, 2, 7, 13, 17, None, 3, None,
            None, None, None, None, None, None, None, 2.5, 4]
    root = TreeNode.create(tree)

    expectedInorderList = [2, 2.5, 3, 4, 5, 7, 10, 13, 15, 17]

    assert list(inorderIterator(root)) == expectedInorderList

    assert list(inorderIterator(TreeNode.create([1, 1]))) == [1, 1]
