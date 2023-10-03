def solution(t, p):
    answer = 0
    num = 0
    length = len(p)
    
    for i in range(len(t)-length+1):    
        num = int(t[i:i+length])
        if num <= int(p):
            answer += 1
    
    return answer