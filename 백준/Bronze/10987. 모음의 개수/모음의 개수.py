import sys
input = sys.stdin.readline

moeum = ['a', 'e', 'i', 'o', 'u']
str = input()
count = 0

for i in str :
    if i in moeum :
        count += 1

print(count)