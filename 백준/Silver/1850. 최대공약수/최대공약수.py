import sys
input = sys.stdin.readline

def gcd(a, b) :
    while b>0 :
        a, b = b, a%b
    return a


A, B = map(int, input().split())
print('1'*int(gcd(A, B)))