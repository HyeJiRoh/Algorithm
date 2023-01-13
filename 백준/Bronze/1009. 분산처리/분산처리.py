import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T) :
    result = 1
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for i in range(b) :
        result = (result*a)%10
    if result == 0:
        result = 10
    print(result)