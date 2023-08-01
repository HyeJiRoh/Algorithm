from itertools import combinations
import sys
sys.stdin.readline

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i+1, j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1, j+1))
            
result = n*2 * len(house)
for comb in list(combinations(chicken, m)):
    dist = 0
    for a, b in house:
        temp = n*2
        for x, y in comb:
            temp = min(temp, abs(a-x) + abs(b-y))
        dist += temp
    result = min(result, dist)
        
print(result)