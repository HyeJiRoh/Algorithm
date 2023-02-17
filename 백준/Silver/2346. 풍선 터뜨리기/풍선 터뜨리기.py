import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(enumerate(map(int, input().split()), start = 1))
result = []

while queue:
    index, num = queue.popleft()
    result.append(index)

    if num>0:
        queue.rotate(-(num-1))
    else:
        queue.rotate(-num)

print(' '.join(map(str, result)))