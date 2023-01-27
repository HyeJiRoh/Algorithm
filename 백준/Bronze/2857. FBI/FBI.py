import sys
input = sys.stdin.readline

name_list = []
count = []

for _ in range(5) :
    name_list.append(input().strip())

for name in name_list :
    if 'FBI' in name :
        count.append(name_list.index(name)+1)

if len(count) == 0 :
    print("HE GOT AWAY!")
else :
    for i in count :
        print(i, end = " ")