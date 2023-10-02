def solution(n):
    answer = ''
    
    while n > 0:
        a, b = divmod(n, 3)
        answer += str(b)
        n = a
        
    return int(answer, 3)