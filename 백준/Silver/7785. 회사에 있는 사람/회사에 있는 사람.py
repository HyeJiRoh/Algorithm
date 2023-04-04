import sys
input = sys.stdin.readline

n = int(input())
name_list = dict()

for _ in range(n):
    name, act = map(str, input().split())
    
    if act == "enter":
        name_list[name] = act
    
    else:
        del name_list[name]

name_list = sorted(name_list.keys(), reverse=True)

for name in name_list:
    print(name)