def solution(n):
    answer = 0
    num = 1
    for i in range(1, 11) :
        num *= i
        if num == n :
            answer = i
        elif num != n and num < n:
            answer = i
    return answer