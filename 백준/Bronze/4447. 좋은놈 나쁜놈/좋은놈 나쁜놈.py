import sys
input = sys.stdin.readline

n = int(input())
name_list = []

for _ in range(n) :
    name = input().strip()
    name_list.append(name)

for i in name_list :
    g = 0
    b = 0
    g += i.count('g')
    g += i.count('G')
    b += i.count('b')
    b += i.count('B')

    if g>b :
        print("%s is GOOD"%i)
    elif b>g :
        print("%s is A BADDY"%i)
    else :
        print("%s is NEUTRAL"%i)