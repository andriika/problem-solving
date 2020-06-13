# https://leetcode.com/problems/lru-cache/

# Implement Least Recently Used (LRU) cache. It should support get and put operations.
#   - get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
#   - put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
#     it should invalidate the least recently used item before inserting a new item.
# The cache is initialized with a positive capacity.


class Node:
    '''
    Doubly Linked List Node
    '''

    def __init__(self, v=None):
        self.v = v
        self.next = self.prev = None

    def remove(self):
        '''
        Remove (detach) itself from the chain
        '''
        p, n = self.prev, self.next
        p.next = n
        n.prev = p

    def insert(self, node):
        '''
        Insert (attach) given node after itself to the chain
        I.e. self.next -> node -> ...
        '''
        n = self.next
        self.next = node
        node.prev = self
        node.next = n
        n.prev = node


class LRUCache(dict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        # We maintain doubly linked list of keys to reflect keys' usage. Least recent used key will always be at the head of the list
        # Sentinel (or Dummy) head and tail nodes are used to simplify list operations. https://en.wikipedia.org/wiki/Linked_list#Using_sentinel_nodes
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        # edge case, return -1 if key is not presented
        if key not in self:
            return -1

        v, node = self[key]
        # move key node to the tail
        node.remove()
        self.tail.prev.insert(node)
        # return key's value
        return v

    def put(self, key: int, value: int) -> None:
        # key exists?
        if key in self:
            _, node = self[key]
            # move key node the tail
            node.remove()
            self.tail.prev.insert(node)
            # replace key's value
            self[key] = value, node
        else:
            # key doesn't exist, let's add it
            # are we at full capacity?
            if len(self) == self.capacity:
                # evict
                evict = self.head.next
                evict.remove()
                del self[evict.v]

            # create key node at the tail of the key list
            node = Node(key)
            self.tail.prev.insert(node)
            # add key, value along with the key node
            self[key] = value, node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
