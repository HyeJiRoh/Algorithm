import sys

input = sys.stdin.readline

N, K = map(int, input().split())

minVal = K*(K+1) // 2

if minVal > N:
    print(-1)
elif (N - minVal) % K == 0:
    print(K-1)
else:
    print(K)