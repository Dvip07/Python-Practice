# Implementing a Priority Queue
# 1.5.1

import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self,item, priority):
        heapq.headpush(self._queue, (-priority, self._index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]

# 1.5.2
class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'. format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('span'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()


# Discussion
a = Item('foo')
b = Item('bar')
a < b
# Traceback (most recent call back)

# --
a = (1, Item('foo'))
b = (5, Item('bar'))
a < b
c = (1, Item('grok'))
a < c

# --
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
a < b
a < c
