import sys

N = int(sys.stdin.readline())
paper = [[0 for j in range(101)] for i in range(101)]

for _ in range(N) :
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            paper[i][j] = 1

result = 0
for i in paper :
    result += i.count(1)

print(result)