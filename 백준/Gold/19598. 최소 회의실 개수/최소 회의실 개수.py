import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = [0]
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort()

for start, end in meetings:
    if start >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))