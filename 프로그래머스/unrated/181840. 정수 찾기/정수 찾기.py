def solution(num_list, n):
    answer = 0
    for i in num_list:
        if i == n:
            answer = 1
            break
    return answer