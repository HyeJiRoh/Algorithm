import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

result = permutations(arr, m)

for data in result:
    for j in data:
        print(j, end = " ")
    print()