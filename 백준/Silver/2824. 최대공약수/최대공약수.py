import sys
input = sys.stdin.readline

def gcd(a, b) :
    while b>0 :
        a, b = b, a%b
    return a

n = 1
N = int(input())
nrr = list(map(int, input().split()))

m = 1
M = int(input())
mrr = list(map(int, input().split()))

for i in nrr :
    n *= i

for i in mrr :
    m *= i

print(str(gcd(n, m))[-9:])