n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(str, input())))

cnt, total = 0, 0
result = ''
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if arr[j][i] == 'T':
            t += 1
        elif arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'C':
            c += 1
            
    if max(a,c,g,t) == a:
        result += 'A'
        total += c + g +t
    elif max(a,c,g,t) == c:
        result += 'C'
        total += a + g +t
    elif max(a,c,g,t) == g:
        result += 'G'
        total += a + c +t
    elif max(a,c,g,t) == t:
        result += 'T'
        total += c + g + a
    
print(result)
print(total)