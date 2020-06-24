# https://leetcode.com/problems/implement-queue-using-stacks



# Idea:
# We push values to the stack1. Now, when it's time to pop, we pop from stack2 that keeps values in a reversed order. 
# I.e. we reverse lifo order into fifo by transfering values from stack1 to stack2 (e.g. while stack1: stack2.push(stack1.pop()))
# This is how queue using 2 stacks works:
#
# Operation     Initial State   Final State     Comment
# ----------------------------------------------------------------------------
# push 1,2,3:   [][]            [1,2,3] []      [][] represents 2 empty stacks
# pop           [1,2,3] []      [] [3,2]        return 1
# push 4,5      [],[3,2]        [4,5][3,2]
# pop           [4,5][3,2]      [4,5][3]        return 2
# push 6        [4,5][3]        [4,5,6][3]
# pop           [4,5,6][3]      [4,5,6][]       return 3
# pop           [4,5,6][]       [][6,5]         return 4
# pop           [][6,5]         [][6]           return 5


class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        return self.s2[-1] if self.s2 else self.s1[0]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
