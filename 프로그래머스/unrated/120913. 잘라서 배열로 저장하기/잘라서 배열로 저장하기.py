def solution(my_str, n):
    answer = []
    string = ''
    cnt = 0
    for word in my_str:
        string += word
        cnt += 1
        if cnt == n :
            answer.append(string)
            string = ''
            cnt = 0
    if len(string) != 0:
        answer.append(string)
    return answer