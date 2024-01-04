import sys
import heapq
input = sys.stdin.readline

n = int(input())
gas_station = [list(map(int, input().split())) for _ in range(n+1)]
gas_station.sort()

base_gas = gas_station[n][1]
current = 0
result = 0
heap = []

for i in range(n+1):
    distance = gas_station[i][0] - current
    current = gas_station[i][0]
    
    if base_gas < distance:
        while base_gas < distance:
            if len(heap) > 0:
                base_gas += (heapq.heappop(heap) * -1)
                result += 1
            else:
                result = -1
                break
        
        if result == -1:
            break
    
    base_gas -= distance
    heapq.heappush(heap, gas_station[i][1] * -1)

print(result)    