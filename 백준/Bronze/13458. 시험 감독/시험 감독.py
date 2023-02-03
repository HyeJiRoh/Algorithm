import sys
from math import ceil
input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
main, sub = map(int, input().split())
count = 0

for i in student:
    if i > main:
        count += ceil((i-main)/sub)
        
print(n+count)