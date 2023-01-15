import sys
input = sys.stdin.readline

while True:
    n = int(input())
    arr = []

    if n == -1 :
        break

    for i in range(1, n) :
        if n%i == 0 :
            arr.append(i)

    if sum(arr) == n :
        print(n, "=", end = " ")
        print(*arr, sep = " + ")
    else :
        print("%d is NOT perfect."%n)