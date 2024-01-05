import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = []
visited = [0] * 10001

for _ in range(n):
    p, d = map(int, input().split())
    lectures.append([p, d])

lectures.sort(key=lambda x: x[1])

q = []

for pay, day in lectures:
    heapq.heappush(q, pay)
    
    if day < len(q):
        heapq.heappop(q)

print(sum(q))