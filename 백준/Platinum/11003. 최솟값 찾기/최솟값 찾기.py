import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()

for i in range(N):
    while q and (q[-1][1] > arr[i]):
        q.pop()
    
    q.append((i+1, arr[i]))
    
    if q[-1][0] - q[0][0] >= L:
        q.popleft()
    
    print(q[0][1], end = " ")