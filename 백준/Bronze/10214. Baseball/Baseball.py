import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    Y = 0
    K = 0

    for k in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k

    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")