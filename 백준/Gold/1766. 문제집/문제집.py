import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = []
result = []

for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)
        
while q:
    cur = heapq.heappop(q)
    result.append(cur)
    
    for g in graph[cur]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            heapq.heappush(q, g)

print(" ".join(map(str, result)))