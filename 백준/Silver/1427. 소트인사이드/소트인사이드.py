import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
n.sort(reverse=True)

for i in n :
    print(i, end="")