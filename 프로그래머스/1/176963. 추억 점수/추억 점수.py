def solution(name, yearning, photo):
    answer = []

    for memory in photo:
        score = 0
        for n in memory:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)

    return answer