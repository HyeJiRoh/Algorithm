import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break

    k = arr[0]
    s = arr[1:]

    arr = list(combinations(s, 6))

    for numbers in arr:
        for num in numbers:
            print(num, end = " ")
        print()
    
    print()