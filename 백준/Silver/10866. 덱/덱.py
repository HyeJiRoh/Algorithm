import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
deque = deque()

for i in range(N) :
    cmd = list(input().split())

    if cmd[0] == "push_front" :
        deque.appendleft(cmd[1])
    elif cmd[0] == "push_back" :
        deque.append(cmd[1])
    elif cmd[0] == "pop_front" :
        if deque :
            print(deque[0])
            deque.popleft()
        else :
            print(-1)
    elif cmd[0] == "pop_back" :
        if deque:
            print(deque[-1])
            deque.pop()
        else:
            print(-1)
    elif cmd[0] == "size" :
        print(len(deque))
    elif cmd[0] == "empty" :
        if deque :
            print(0)
        else :
            print(1)
    elif cmd[0] == "front" :
        if deque :
            print(deque[0])
        else :
            print(-1)
    elif cmd[0] == "back" :
        if deque:
            print(deque[-1])
        else:
            print(-1)