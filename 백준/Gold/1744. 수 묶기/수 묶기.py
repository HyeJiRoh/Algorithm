import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

arr = []
brr = []
res = 0

for _ in range(N):
    x = int(input())
    if x <= 0:
        brr.append(x)
    elif x == 1:
        res += 1
    else:
        arr.append(x)
        
brr.sort()
arr.sort(reverse = True)

if len(arr) % 2 !=0:
    arr.append(1)
if len(brr) % 2 !=0:
    brr.append(1)
    
for i in range(0, len(arr),2):
    res += (arr[i] * arr[i+1])
    
for i in range(0, len(brr),2):
    res += (brr[i] * brr[i+1])
    
print(res)