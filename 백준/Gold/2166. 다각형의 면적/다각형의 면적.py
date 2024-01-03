import sys
input = sys.stdin.readline

n = int(input())
x = []
y = []

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    
x.append(x[0])
y.append(y[0])

_x, _y = 0, 0

for i in range(n):
    _x += x[i]*y[i+1]
    _y += x[i+1]*y[i]

print(round(abs(_x-_y)/2, 1))