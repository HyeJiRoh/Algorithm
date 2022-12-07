def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == 1 :
            answer += absolutes[i]
        elif signs[i] == 0 :
            answer -= absolutes[i]
    return answer