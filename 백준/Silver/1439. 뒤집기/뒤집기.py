import sys
input = sys.stdin.readline

str = list(input().strip())
count = 0

for i in range(len(str)-1) :
    if str[i] != str[i+1] :
        count += 1
        
print((count+1)//2)