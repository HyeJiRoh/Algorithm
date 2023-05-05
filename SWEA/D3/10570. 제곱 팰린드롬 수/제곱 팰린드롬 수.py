import math

T = int(input())

def palindrome(num):
    if len(num) < 2:
        return True
    
    if num[0] != num[-1]:
        return False
    
    return palindrome(num[1:-1])

for idx in range(1, T + 1):
    cnt = 0

    a, b = map(int, input().split())

    for i in range(a, b + 1):
        if palindrome(str(i)):
            num = int(math.sqrt(i))
            if num ** 2 == i and palindrome(str(num)):
                cnt += 1
    
    print("#%d %d"%(idx, cnt))