import sys
input = sys.stdin.readline

R, C = map(int, input().split())

filter = []

for _ in range(R):
    filter.append(list(map(int, input().split())))

T = int(input())

cnt = 0

for i in range(R-2):
    for j in range(C-2):
        check = []
        for k in range(i, i+3):
            for l in range(j, j+3):
                check.append(filter[k][l])
              
        check.sort()

        if check[4] >= T:
            cnt += 1

print(cnt)