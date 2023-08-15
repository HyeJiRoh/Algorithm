import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

if max(visitors) == 0:
    print("SAD")

else:
    max_visit = sum(visitors[0:x])
    value = max_visit
    cnt = 1

    for i in range(x, n):
        value -= visitors[i - x]
        value += visitors[i]

        if value > max_visit:
            max_visit = value
            cnt = 1
        elif value == max_visit:
            cnt += 1

    print(max_visit)
    print(cnt)
