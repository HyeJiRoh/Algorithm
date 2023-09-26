import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    price = int(input())
    result = [0, 0, 0, 0]

    while True:
        if price == 0:
            break

        if price >= 25:
            result[0] = price // 25
            price -= result[0] * 25
        elif price >= 10:
            result[1] = price // 10
            price -= result[1] * 10
        elif price >= 5:
            result[2] = price // 5
            price -= result[2] * 5
        elif price >= 1:
            result[3] = price // 1
            price -= result[3] * 1

    print(*result)
