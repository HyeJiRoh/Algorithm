import sys
input = sys.stdin.readline

N = int(input())

drink = list(map(int, input().split()))

drink.sort(reverse=True)

total = drink[0]

for i in range(1, N):
  total += drink[i] / 2

print('%g' % total) 