def solution(n):
    answer = 0
    if n <= 7:
        answer = 1
    elif n % 7 == 0 :
        answer = n//7
    else :
        answer = (n//7)+1
    return answer