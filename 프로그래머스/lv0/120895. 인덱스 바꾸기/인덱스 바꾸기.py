def solution(my_string, num1, num2):
    answer = ''
    str = []
    for i in my_string :
        str.append(i)
    temp = str[num1]
    str[num1] = str[num2]
    str[num2] = temp
    for i in str :
        answer += i
    return answer