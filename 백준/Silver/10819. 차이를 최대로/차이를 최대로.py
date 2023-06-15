import sys 
from itertools import permutations 

input = sys.stdin.readline 
n = int(input()) 

arr = list(map(int, input().split())) 
p = list(permutations(arr, n)) 
answer = 0 

for i in p: 
    s = 0 
    for j in range(n-1): 
        s += abs(i[j] - i[j+1]) 
    
    answer = max(answer, s) 

print(answer)