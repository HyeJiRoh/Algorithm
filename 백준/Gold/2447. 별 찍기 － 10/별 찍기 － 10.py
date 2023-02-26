def draw(n):
    tmp =[]     					
    for i in range(3 * len(n)):    
        if i // len(n) == 1:        
            tmp.append(n[i%len(n)] + " " * len(n) + n[i%len(n)])
        else:
            tmp.append(n[i%len(n)] * 3)
    return tmp

star = ["***", "* *", "***"]    
N = int(input())
cnt = 0

while N != 3:       
    N = N // 3
    cnt += 1        

for _ in range(cnt):	
    star = draw(star)   

for i in star:     
    print(i)