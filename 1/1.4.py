# # Finding the Largest or smallest N Items
# # 1.4.1


# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37,2]
# print(heapq.nlargest(3, nums)) 
# print(heapq.nsmallest(3, nums))

# 1.4.2
from email import header
import heapq
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# Discussion
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
heap

# --
heap.heappop(heap)
heap.heappop(heap)
heap.heappop(heap)