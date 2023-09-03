import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())

X, Y = min(X, Y), max(X, Y)

if S < W * 2:
    s, b = min(X, Y), max(X, Y)
    if S <= W:
        m = (X+Y)%2
        print((Y-m)*S + m*W)
    else:
        print(X*S + (Y-X)*W)
else:
    print((X+Y)*W)