import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for num in arr :
    total = 0
    num = int(num)
    for i in range(1, num):
        if num%i == 0:
            total += i
    if total == num:
        print("Perfect")
    elif total < num:
        print("Deficient")
    elif total > num:
        print("Abundant")