from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

def bfs():
    queue = deque([S])
    
    while queue:
        now = queue.popleft()

        if now == G:
            return visited[now]
        
        for choice in (now - D, now + U):
            if 0 < choice <= F and not visited[choice] and choice != S:
                visited[choice] = visited[now] + 1
                queue.append(choice)

    else:
        return "use the stairs"

visited = [0] * (F + 1)

print(bfs())