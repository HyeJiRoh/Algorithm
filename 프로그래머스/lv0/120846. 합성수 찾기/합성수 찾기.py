def solution(n):
    answer = 0
    for i in range(1, n+1) :
        count = 0
        for k in range(1, n+1) :
            if i%k == 0 :
                count +=1
        if count >= 3 :
            answer += 1
    return answer