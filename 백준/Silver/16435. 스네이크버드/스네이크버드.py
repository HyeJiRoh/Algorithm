import sys
input = sys.stdin.readline

n, l = map(int, input().split())
fruits = list(map(int, input().split()))
fruits.sort()

for fruit in fruits:
    if l >= fruit:
        l += 1
    else:
        break

print(l)