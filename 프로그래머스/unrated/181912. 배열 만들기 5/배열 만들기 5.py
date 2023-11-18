def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        tmp = int(num[s:s+l])
        if tmp > k:
            answer.append(tmp)
    return answer