import heapq
import sys

n = int(sys.stdin.readline())

heap = []
q = []
count = 0

for _ in range(n):
    num, start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(heap, [start,end,num])

start, end, num = heapq.heappop(heap)
heapq.heappush(q, end)

while heap:
    start, end, num = heapq.heappop(heap)
    if q[0] <= start:
        heapq.heappop(q)
    heapq.heappush(q, end)

print(len(q))