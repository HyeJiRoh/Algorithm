def solution(my_string):
    answer = ''
    temp = []
    for i in my_string :
        if i not in temp :
            temp.append(i)
    answer = "".join(temp)
    return answer