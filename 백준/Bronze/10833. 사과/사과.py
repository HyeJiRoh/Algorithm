import sys
input = sys.stdin.readline

n = int(input())
result = 0

for _ in range(n):
    student, apple = map(int, input().split())
    
    if apple >= student:
        apple = apple % student
    
    result += apple

print(result)