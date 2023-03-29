import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())

time = int(input())

a = (p + time) // w
b = (q + time) // h

if a % 2 == 0:
    num1 = (p + time) % w
else:
    num1 = w - (p + time) % w

if b % 2 == 0:
    num2 = (q + time) % h
else:
    num2 = h - (q + time) % h

print(num1, num2)