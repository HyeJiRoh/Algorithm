import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

sensors.sort()
arr = []

for i in range(len(sensors)-1):
    arr.append(sensors[i+1] - sensors[i])

arr.sort()

print(sum(arr[:n-k]))