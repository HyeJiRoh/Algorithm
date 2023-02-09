t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    room = n % h
    if n % h == 0: 
        num = n//h
        room = h
    print(f'{room*100+num}')