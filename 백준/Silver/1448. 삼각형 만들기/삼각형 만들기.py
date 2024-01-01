import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

stack = []
flag = False
total = 0

while True:
    if flag or len(nums)==2:
        break
    
    stack.append(nums.pop())
    
    if nums[-1] + nums[-2] > stack[-1]:
        total = nums[-1] + nums[-2] + stack[-1]
        flag = True
    
    else:
        stack.pop()

if flag == False:
    print(-1)
else:
    print(total)