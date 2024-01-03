import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
gems = []

for _ in range(n):
    m, v = map(int, input().split())
    gems.append([m, v])

gems.sort()

C = [int(input()) for _ in range(k)]
C.sort()

tmp = []
result = 0

for c in C:
    while gems and c >= gems[0][0]:
            heapq.heappush(tmp, -gems[0][1])
            heapq.heappop(gems)
    
    if tmp:
        result += heapq.heappop(tmp)

print(-result)