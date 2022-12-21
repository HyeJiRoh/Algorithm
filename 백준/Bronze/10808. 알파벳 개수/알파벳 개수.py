s = list(input())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr = []

for i in alpha :
    if i in s :
        arr.append(s.count(i))
    else :
        arr.append(0)

for i in arr :
    print(i, end=' ')