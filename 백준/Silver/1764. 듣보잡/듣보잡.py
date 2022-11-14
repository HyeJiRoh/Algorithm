import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = set([input().strip() for i in range(n)])
brr = set([input().strip() for i in range(m)])

count = 0
result = []

if n<=m :
  for i in arr :
    if i in brr :
      count += 1
      result.append(i)

result.sort()

print(count)

for i in result :
  print(i)