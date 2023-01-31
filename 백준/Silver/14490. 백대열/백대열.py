import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split(':'))
a = math.gcd(n, m)
print("%d:%d"%(n//a, m//a))