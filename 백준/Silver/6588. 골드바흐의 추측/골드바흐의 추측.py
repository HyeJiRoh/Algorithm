import sys

input = sys.stdin.readline

sosu = [True] * 1000001
m = int(1000001**0.5)
for i in range(2, m + 1):
    if sosu[i]:
        for k in range(i + i, 1000001, i):
            sosu[k] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(2, m + 3):
            if sosu[i] and sosu[n - i]:
                print("%d = %d + %d" % (n, i, n - i))
                break
