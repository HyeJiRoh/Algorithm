import sys
input = sys.stdin.readline

num = int(input())
arr = []

for i in range(num) :
  x, y = map(int, input().split())
  arr.append((x, y))
  
arr.sort()

for i in arr :
  print(i[0], i[1])