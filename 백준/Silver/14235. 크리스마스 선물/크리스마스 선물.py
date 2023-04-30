import heapq
import sys
input = sys.stdin.readline

n = int(input())
gift = []

for i in range(n):
    a = list(map(int, input().split()))
    
    if a[0] == 0:
        if len(gift) == 0:
            print(-1)
        else:
            temp = -(heapq.heappop(gift))
            print(temp)
    else:
        for j in range(a[0]):
            heapq.heappush(gift, -(a[j+1]))