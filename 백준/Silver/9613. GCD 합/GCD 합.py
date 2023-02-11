import sys
import math
input = sys.stdin.readline

repeat = int(input())

for i in range(repeat):
    arr = list(map(int, input().split()))
    total = 0

    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            total += math.gcd(arr[i], arr[j])

    print(total)