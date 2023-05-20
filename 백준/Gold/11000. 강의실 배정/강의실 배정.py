import heapq
import sys
input = sys.stdin.readline

n = int(input())

rooms = [list(map(int, input().split())) for _ in range(n)]
heap = [0]

rooms.sort()

for start, end in rooms:
    if start >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))