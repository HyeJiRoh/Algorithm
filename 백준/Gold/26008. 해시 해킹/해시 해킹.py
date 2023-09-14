import sys
input = sys.stdin.readline

N, M, A = map(int, input().split())
H = int(input())

print(pow(M, N - 1, 1000000007))
