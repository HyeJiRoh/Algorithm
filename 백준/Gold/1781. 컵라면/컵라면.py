import sys
import heapq
input = sys.stdin.readline

N = int(input())
homeworks = []

for _ in range(N):
    deadline, cup = map(int, input().split())
    homeworks.append([deadline, cup])

homeworks.sort(key=lambda x:(x[0], -x[1]))

cup_heap = []

for homework in homeworks:
    heapq.heappush(cup_heap, homework[1])
    if len(cup_heap) > homework[0]:
        heapq.heappop(cup_heap)
    
print(sum(cup_heap))