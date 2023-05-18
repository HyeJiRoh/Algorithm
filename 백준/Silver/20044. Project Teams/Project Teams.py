import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = []

for i in range(n):
    result.append(max(arr) + min(arr))
    arr.remove(max(arr))
    arr.remove(min(arr))

print(min(result))