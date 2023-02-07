from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([])

for i in range(1, N+1):
    queue.append(i)

result = []
count = 1

while queue:
    if count%K == 0:
        result.append(str(queue.popleft()))
    else:
        queue.append(queue.popleft())
    count += 1

print("<%s>"%(", ").join(result))