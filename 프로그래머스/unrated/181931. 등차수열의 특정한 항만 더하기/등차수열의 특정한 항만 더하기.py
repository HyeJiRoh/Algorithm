def solution(a, d, included):
    answer = 0
    gap = a
    if included[0]:
        answer += a
    for idx in range(1, len(included)):
        gap += d
        if included[idx]:
            answer += gap
    return answer