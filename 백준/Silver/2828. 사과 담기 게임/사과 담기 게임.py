n,m = map(int, input().split())
j = int(input())
 
left = 1
right = m
count = 0
 
for _ in range(j):
    position = int(input())
 
    if left <= position and right >= position:
        continue
    elif left > position:
        count += (left-position)
        right -= (left-position)
        left = position
    else:
        count += (position-right)
        left += (position-right)
        right = position
 
print(count)