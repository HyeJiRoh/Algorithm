import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = [num for num in range(1, n + 1)]

for numbers in permutations(arr):
    for num in numbers:
        print(num, end = ' ')
    print()
