import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = set([input().strip() for _ in range(n)])
count = 0

for _ in range(m) :
  i = input().strip()
  if i in arr :
    count += 1

print(count)