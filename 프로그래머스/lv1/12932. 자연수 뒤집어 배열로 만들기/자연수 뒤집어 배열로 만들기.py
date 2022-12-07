def solution(n):
    answer = []
    n = list(str(n))
    for i in range(len(n)//2) :
        base = len(n)//2
        temp = n[i]
        n[i] = n[-i-1]
        n[-i-1] = temp
    for i in n :
        answer.append(int(i))
    return answer