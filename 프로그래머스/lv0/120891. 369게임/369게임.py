def solution(order):
    answer = 0
    order = list(str(order))
    for i in order :
        i = int(i)
        if i%3 == 0 and i!=0 :
            answer +=1
            
    return answer