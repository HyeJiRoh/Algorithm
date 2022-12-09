def solution(i, j, k):
    answer = ''
    for a in range(i, j+1) :
        a = str(a)
        answer += a
    k = str(k)
    return answer.count(k)