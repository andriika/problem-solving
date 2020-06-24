# https://leetcode.com/problems/implement-stack-using-queues/


import collections

# Idea:
# We push values to the queue. When it's time to pop, we "re-push" all values but the last one, 
# so that the last pushed value appears in the front of the queue. For example:
# 
# Let queue = [d, c, b, a] be a queue, where 'a' in the front, 'b' is the next one, 'c' is thr next one, and 'd' is in the tail.
# After repushing, the queue looks like following: [c, b, a, d]. Now we can easily pop 'd' and return it.
# After popping 'd', the queue have the same order as in the beggining but w/o 'd' value: [c, b, a]

class MyStack:

    def __init__(self):
        self.q = collections.deque()
        self._top = None # keeps last pushed element of the stack

    def push(self, x: int) -> None:
        self._top = x
        self.q.appendleft(x)

    def pop(self) -> int:

        self._top = None # reset top element to avoid memory leaks

        # re-push all elements but the last one
        n = len(self.q) - 1
        while n > 0:
            x = self.q.pop()
            self.push(x)
            n -= 1

        # after re-pushing, the last pushed element becomes 1-st in the queue
        # pop it and return
        return self.q.pop()

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
