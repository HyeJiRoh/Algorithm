import sys
input = sys.stdin.readline

n = int(input())
villages = []
total_people = 0

for _ in range(n):
    location, people = map(int, input().split())
    villages.append([location, people])
    total_people += people

villages.sort(key = lambda x: x[0])
cnt = 0

for i in range(n):
    cnt += villages[i][1]
    
    if cnt >= total_people/2:
        print(villages[i][0])
        break