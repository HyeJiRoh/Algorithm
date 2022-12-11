def solution(x):
    answer = True
    total = 0
    
    for i in str(x) :
        i = int(i)
        total += i
   
    if x%total != 0 :
        answer = False
        
    return answer