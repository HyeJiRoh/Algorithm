import sys
from math import gcd
input = sys.stdin.readline

a, b = map(int, input().split())
x, y = map(int, input().split())

result_a = (a * y) + (b * x)
result_b = b * y

max_gcd = gcd(result_a, result_b)

if max_gcd != 1:
    result_a = result_a // max_gcd
    result_b = result_b // max_gcd
    print(result_a, result_b)
elif max_gcd == 1:
    print(result_a, result_b)
