import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()
arr = []

for i in range(len(heights)-1):
    arr.append(heights[i+1]-heights[i])

arr.sort()

print(sum(arr[:n-k]))