def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        tmp = 1
        for num in num_list:
            tmp *= num
        answer = tmp
    return answer