def solution(num_list):
    answer = -1
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
    return answer