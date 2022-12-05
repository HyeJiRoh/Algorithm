def solution(num, k):
    answer = -1
    num = list(str(num))
    for i in num :
        if int(i) == k :
            answer = num.index(i)+1   
    return answer