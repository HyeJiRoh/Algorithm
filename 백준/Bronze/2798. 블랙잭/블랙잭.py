n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for i in range(len(arr)) :
  for k in range(i+1, len(arr)) :
    for l in range(k+1, len(arr)) :
      sum = arr[i]+arr[k]+arr[l]
      if sum > m :
        continue
      else :
        result = max(result, sum)

print(result)