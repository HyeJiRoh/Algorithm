from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([n])

    while queue:
        now = queue.popleft()

        if now == k:
            return arr[now]
        
        for next in (now - 1, now + 1, now * 2):
            if 0 <= next <= MAX and not arr[next]:
                arr[next] = arr[now] + 1
                queue.append(next)

n, k = map(int, input().split())
MAX = 100000
arr = [0] * (MAX + 1)

print(bfs())