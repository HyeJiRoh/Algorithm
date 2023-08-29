import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

visit = [0 for _ in range(V + 1)]
heap = [[0, 1]]

result = 0
cnt = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

while heap:
    if cnt == V:
        break

    C, B = heapq.heappop(heap)

    if visit[B] == 0:
        visit[B] = 1
        result += C
        cnt += 1

        for i in graph[B]:
            heapq.heappush(heap, i)

print(result)
