import sys
input = sys.stdin.readline

N = int(input())
str = list(input().strip())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
square_num = 0
result = 0

for i in str :
    if i in alpha :
        num = alpha.index(i)
        result += (num+1)*(31**square_num)
        square_num += 1

print(result)