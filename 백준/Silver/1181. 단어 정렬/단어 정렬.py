import sys

num = int(sys.stdin.readline())
arr = []

for i in range(num) :           
  arr.append(sys.stdin.readline().strip())

arr = list(set(arr))
arr.sort(key = lambda x:(len(x),x))

for i in arr :
  print(i)