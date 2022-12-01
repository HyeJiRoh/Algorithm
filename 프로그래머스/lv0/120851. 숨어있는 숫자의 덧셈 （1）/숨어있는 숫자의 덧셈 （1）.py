def solution(my_string):
    answer = 0
    for i in my_string :
        if i.isdigit() == True :
            answer += int(i)
        else :
            continue
    return answer