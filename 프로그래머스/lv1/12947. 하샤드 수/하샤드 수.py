def solution(x):
    answer = True
    temp = 0
    num = x
    while (x>=10) :
        temp += x%10
        x = x//10
    temp += x
    if num%temp == 0 :
        answer= True
    else :
        answer = False
    return answer