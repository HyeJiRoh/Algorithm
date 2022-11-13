import sys
input = sys.stdin.readline

num = int(input())
arr = []

for i in range(num) :
  a, b = input().split()
  a = int(a)
  arr.append((a, b))

arr.sort(key = lambda x : x[0])

for i in arr :
  print(i[0], i[1])