import sys

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    arr = sys.stdin.readline().split()

    if arr[0] == "push":
        queue.insert(0, arr[1])

    elif arr[0] == "pop":
        if len(queue) != 0: print(queue.pop())
        else: print(-1)

    elif arr[0] == "size":
        print(len(queue))

    elif arr[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)

    elif arr[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])

    elif arr[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])