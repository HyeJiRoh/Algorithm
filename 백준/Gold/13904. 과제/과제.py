import sys
input = sys.stdin.readline

n = int(input())
homeworks = []
visit = [0] * 1001

for _ in range(n):
    day, score = map(int, input().split())
    homeworks.append([day, score])

homeworks.sort(key=lambda x: -x[1])
result = 0

for day, score in homeworks:
    base = day
    
    while base > 0 and visit[base]:
        base -= 1
    
    if base == 0:
        continue
    else:
        visit[base] = 1
        result += score

print(result)