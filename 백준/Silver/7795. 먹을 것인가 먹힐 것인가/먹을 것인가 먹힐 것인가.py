import sys
import bisect
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    count = 0

    for num in a:
        count += (bisect.bisect(b, num - 1))
    print(count)