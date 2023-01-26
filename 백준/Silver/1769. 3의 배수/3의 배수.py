import sys
input = sys.stdin.readline

x = list(map(int, input().strip()))
count = 0

while len(x) > 1:
    temp = []
    count += 1

    x = sum(x)
    for i in str(x):
        temp.append(int(i))

    x = temp
    
print(count)

if x[0]%3 == 0 :
    print("YES")
else :
    print("NO")