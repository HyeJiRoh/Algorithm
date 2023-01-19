import sys
input = sys.stdin.readline

n = int(input())
a=b=100

for i in range(n) :
    chang, sang = map(int, input().split())
    if chang>sang :
        b -= chang
    elif sang>chang :
        a -= sang

print(a)
print(b)