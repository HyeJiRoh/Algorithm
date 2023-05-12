import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    num = int(input())
    
    if num != 0:
        result.append(num)
    else:
        result.pop()

if len(result) == 0:
    print(0)
else:
    print(sum(result))