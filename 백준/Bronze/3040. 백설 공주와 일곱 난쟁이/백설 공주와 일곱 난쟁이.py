dwarf = [int(input()) for _ in range(9)]
answer = False
    
for i in range(8):
    if answer: 
        break
        
    for j in range(i+1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100: 
            dwarf.pop(i)
            dwarf.pop(j-1)
            
            for k in sorted(dwarf):
                print(k)
                
            answer = True
            break