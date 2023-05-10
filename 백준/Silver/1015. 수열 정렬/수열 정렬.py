import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))
sorted_array = sorted(array)

result = [0] * n

for i in range(n):
  idx = sorted_array.index(array[i])
  result[i] = idx
  sorted_array[idx] = -1

print(*result)