n = int(input())
arr = set(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

for i in brr :
  if i in arr :
    print(1)
  else :
    print(0)