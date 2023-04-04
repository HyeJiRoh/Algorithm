import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
numbers = list(map(int, input().split()))

cnt = 0

numbers.sort()

start, end = 0, n-1

while start < end:
    if numbers[start] + numbers[end] == m:
        cnt += 1
        start += 1
        end -= 1
    
    elif numbers[start] + numbers[end] < m:
        start += 1
    
    else:
        end -= 1

print(cnt)