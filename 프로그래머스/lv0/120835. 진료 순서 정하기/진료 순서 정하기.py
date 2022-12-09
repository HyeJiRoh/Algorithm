def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse = True)
    print(temp)
    for i in range(len(emergency)) :
        for k in temp :
            if emergency[i] == k :
                answer.append(temp.index(k)+1)
    return answer