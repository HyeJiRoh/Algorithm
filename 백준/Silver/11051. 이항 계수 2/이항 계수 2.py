import sys
import math
input = sys.stdin.readline

N, K = map(int, input().split())
result = math.comb(N, K)%10007

print(result)