from collections import deque

N, K, M = map(int, input().split())
queue = deque(range(1, N+1))
i = 0

while queue:
    if i // M % 2 == 0:
        for _ in range(K-1):
            queue.append(queue.popleft())
    else:
        for _ in range(K):
            queue.appendleft(queue.pop())
    i += 1
    print(queue.popleft())