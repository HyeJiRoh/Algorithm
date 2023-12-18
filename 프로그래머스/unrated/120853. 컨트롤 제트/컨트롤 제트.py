def solution(s):
    answer = 0
    s_arr = s.split()
    for i in range(len(s_arr)):
        if s_arr[i] == "Z":
            answer -= int(s_arr[i-1])
        else:
            answer += int(s_arr[i])
    return answer