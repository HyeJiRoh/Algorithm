import sys
input = sys.stdin.readline

N = int(input())

for i in range(N) :
    r, e, c = map(int, input().split())
    margin = e-c

    if r > margin :
        print("do not advertise")
    elif r == margin :
        print("does not matter")
    else :
        print("advertise")