def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(1, n+1):
            if i % 2 != 0:
                answer += i
    else:
        for i in range(1, n+1):
            if i % 2 == 0:
                answer += i**2
    return answer