import sys
input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))

stones.sort()
target = 1

for num in stones:
    if target < num:
        break
    
    target += num
    
print(target)