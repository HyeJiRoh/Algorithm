import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = []

result.append(sum(arr[:k]))

for i in range(0, len(arr) - k):
    result.append(result[i] - arr[i] + arr[i + k])

print(max(result))