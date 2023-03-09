import sys
input = sys.stdin.readline

def power(a, n, c):
    if n == 0:
        return 1
    
    x = power(a, n//2, c)

    if n % 2 == 0:
        return (x * x) % c
    
    else:
        return (x * x * a) % c

a, b, c = map(int, input().split())
print(power(a, b, c))