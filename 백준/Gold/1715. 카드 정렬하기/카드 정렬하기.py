import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

result = 0

if len(heap) == 1:
    print(0)

else:
    while len(heap) > 1:
        card1 = heapq.heappop(heap)
        card2 = heapq.heappop(heap)

        result += card1 + card2

        heapq.heappush(heap, card1 + card2)

    print(result)