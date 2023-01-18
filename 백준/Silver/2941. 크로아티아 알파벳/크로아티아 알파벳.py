import sys
input = sys.stdin.readline

str = input().strip()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha :
    str = str.replace(i, '@')

print(len(str))