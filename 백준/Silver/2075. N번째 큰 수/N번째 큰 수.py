import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    numbers = map(int, input().split())

    if not heap:
        for number in numbers:
            heapq.heappush(heap, number)
    
    else:
        for number in numbers:
            if heap[0] < number:
                heapq.heappush(heap, number)
                heapq.heappop(heap)
    
print(heap[0])