def solution(n):
    answer = ''
    for i in range(n) :
        if i%2 == 0 :
            answer += '수'
        elif i%2 != 0 :
            answer += '박'
    return answer