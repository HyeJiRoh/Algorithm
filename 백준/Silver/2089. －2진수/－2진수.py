n = int(input())
res = ''

if n == 0:
    print(0)
    exit()
    
while n:
    if n % (-2):
        res = '1' + res
        n = n//-2 + 1
    else:
        res = '0' + res
        n = n//-2

print(res)