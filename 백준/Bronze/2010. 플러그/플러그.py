import sys
input = sys.stdin.readline

N = int(input())
plug = 0

for i in range(N) :
    i = int(input())
    plug += (i-1)

print(plug+1)