import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

count = Counter(arr)

for k in brr :
  if k in count :
    print(count[k], end = ' ')
  else :  
    print(0, end = ' ')