import math
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
water = []
cnt = 0

for _ in range(n):
    start, end = map(int, input().split())
    water.append([start, end])

water.sort()
base = water[0][0]

for start, end in water:
    while True:
        if base >= end:
            break
        if base < start:
            base = start
        else:
            base += k
            cnt += 1
        
print(cnt)