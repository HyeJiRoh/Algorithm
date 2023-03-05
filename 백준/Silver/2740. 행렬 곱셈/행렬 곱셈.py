import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nrr = [list(map(int, input().split())) for i in range(n)]

m, k = map(int, input().split())
mrr = [list(map(int, input().split())) for i in range(m)]

for i in range(n):
    result = []
    for l in range(k):
        num = 0
        for j in range(m):
            num += nrr[i][j] * mrr[j][l]
        result.append(num)
    print(*result)