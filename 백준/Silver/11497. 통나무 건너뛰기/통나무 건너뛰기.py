import sys

input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    result = [0] * n
    result[n // 2] = arr[0]

    for i in range(1, n):
        if i % 2 == 1:
            result[n // 2 - i // 2 - 1] = arr[i]
        else:
            result[n // 2 + i // 2] = arr[i]

    max_value = 0

    for i in range(n):
        value = abs(result[i] - result[(i + 1) % n])
        max_value = max(max_value, value)

    print(max_value)
