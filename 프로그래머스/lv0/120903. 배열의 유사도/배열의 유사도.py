def solution(s1, s2):
    answer = 0
    for i in s1 :
        for k in s2 :
            if i == k :
                answer +=1
    return answer