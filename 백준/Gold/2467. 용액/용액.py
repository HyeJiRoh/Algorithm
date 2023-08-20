import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
max_value = 2000000000
left = 0
right = N-1
x, y = 0, 0

while left < right:
    tmp_value = liquids[left] + liquids[right]
    
    if abs(tmp_value) <= max_value:
        x = liquids[left]
        y = liquids[right]
        max_value = abs(tmp_value)
    
    if tmp_value <= 0:
        left += 1
    
    else:
        right -= 1

print(x, y)