import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    
    if x != 0:
        heapq.heappush(q, x)
    else:
        if len(q) == 0:
            print(0)
            continue
        else:
            print(heapq.heappop(q))