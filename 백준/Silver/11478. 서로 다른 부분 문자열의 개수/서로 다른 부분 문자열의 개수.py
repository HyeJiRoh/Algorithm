import sys
input = sys.stdin.readline

s = input().strip()
arr = set()

for i in range(len(s)) :
  for k in range(i, len(s)) :
    arr.add(s[i:k+1])

print(len(arr))