import sys

T = int(input())

for _ in range(T):
    wear = {}
    result = 1
    n = int(input())
    for _ in range(n):
        name, type = map(str, input().split())

        if not type in wear:
            wear[type] = 1
        else:
            wear[type] += 1

    for i in wear:
        result *= (wear[i] + 1)

    print(result - 1)