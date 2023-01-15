import sys
input = sys.stdin.readline

N = int(input())
total = 0

for i in range(N+1, N**2, N+1) :
    if i%N == i//N :
        total += i

print(total)