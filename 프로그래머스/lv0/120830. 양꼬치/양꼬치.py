def solution(n, k):
    sheep = 12000
    drink = 2000
    service = n//10
    if n >= 10 :
        answer = sheep*n + drink*k - drink*service
    else :
        answer = sheep*n + drink*k
    return answer