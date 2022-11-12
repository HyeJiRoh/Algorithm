import sys
input = sys.stdin.readline

num = int(input())
arr = []

for i in range(num) :
  arr.append(int(input()))

arr.sort()

for i in arr:
  print(int(i))