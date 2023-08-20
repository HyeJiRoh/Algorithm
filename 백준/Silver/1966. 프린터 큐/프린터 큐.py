import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))
    cnt = 0
    
    while queue:
        if queue[0] == max(queue):
            cnt += 1
            queue.popleft()
            current_idx = idx.popleft()
            if current_idx == m:
                print(cnt)
                
        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())