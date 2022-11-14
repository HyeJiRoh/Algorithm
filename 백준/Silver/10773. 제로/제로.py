import sys
input = sys.stdin.readline

k = int(input())
arr = []

for i in range(k) :
  i = int(input())
  if i == 0 :
    arr.pop()
  else : 
    arr.append(i)


print(sum(arr))