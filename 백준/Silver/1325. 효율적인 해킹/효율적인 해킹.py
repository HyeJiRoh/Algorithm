from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
computer = [[] for _ in range(n+1)]

for _ in range(m):
    b, a = map(int, input().split())
    computer[a].append(b)

result = []
max_cnt = -1

def bfs(node):
    global count
    queue = deque([node])
    visited = [False for _ in range(n+1)]
    visited[node] = True

    while queue:
        node = queue.popleft()

        for idx in computer[node]:
            if not visited[idx]:
                queue.append(idx)
                visited[idx] = True
                count += 1
    
    return count

for i in range(1, n+1):
    count = 0
    com = bfs(i)

    if com > max_cnt:
        result = [i]
        max_cnt = com
    
    elif com == max_cnt:
        result.append(i)
        max_cnt = com

print(*result, end = ' ')