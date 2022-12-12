def solution(n):
    answer = []
    i = 2
    while n != 1 :
        if n%i :
            i+=1
        else :
            answer.append(i)
            n = n//i
    answer = list(set(answer))
    answer.sort()
    return answer