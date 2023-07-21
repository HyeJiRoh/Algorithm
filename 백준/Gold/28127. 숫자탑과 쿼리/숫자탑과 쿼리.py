import sys

input = sys.stdin.readline


def binarySearch(x):
    start, end = 1, x

    while True:
        mid = (start + end) // 2

        if (
            (mid - 1) * (2 * a + ((mid - 1) - 1) * d) // 2
            < x
            <= (mid) * (2 * a + ((mid) - 1) * d) // 2
        ):
            return mid

        if (mid) * (2 * a + ((mid) - 1) * d) // 2 < x:
            start = mid + 1
        else:
            end = mid - 1

Q = int(input())

for _ in range(Q):
    a, d, x = map(int, input().split())

    floor = binarySearch(x)

    cnt = a + (floor - 1) * d
    e = (floor) * (2 * a + ((floor) - 1) * d) // 2

    left_cnt = cnt - (e - x)

    print(floor, left_cnt)
