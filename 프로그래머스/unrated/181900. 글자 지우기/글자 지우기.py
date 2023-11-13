def solution(my_string, indices):
    answer = ''
    for idx in range(len(my_string)):
        if idx not in indices:
            answer += my_string[idx]
    return answer