def solution(str_list):
    answer = []
    for idx in range(len(str_list)):
        if str_list[idx] == "l":
            answer = str_list[:idx]
            break
        elif str_list[idx] == "r":
            answer = str_list[idx+1:]
            break
        else:
            answer = []
    return answer