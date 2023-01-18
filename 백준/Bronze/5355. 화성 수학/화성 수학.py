import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) :
  arr = list(map(str, input().strip().split()))
  arr[0] = float(arr[0])
  
  for k in range(1, len(arr)) :
    if arr[k] == '@' :
      arr[0] *= 3
    elif arr[k] == '%' :
      arr[0] += 5
    elif arr[k] == '#' :
      arr[0] -= 7
      
  print('%.2f'%arr[0])