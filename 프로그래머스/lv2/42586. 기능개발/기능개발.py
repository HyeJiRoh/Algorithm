def solution(progresses, speeds):
    answer = []
    day = [0 for _ in range(len(progresses))]
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            day[i] = (100 - progresses[i]) // speeds[i] + 1
        else:
            day[i] = (100 - progresses[i]) // speeds[i]

    tmp = []
    
    for i in range(len(day)):
        if len(tmp) == 0:
            tmp.insert(0, day[i])
        elif tmp[-1] < day[i]:
            answer.append(len(tmp))
            tmp.clear()
            tmp.insert(0, day[i])
        else:
            tmp.insert(0, day[i])
    
    if len(tmp) != 0:
        answer.append(len(tmp))
        tmp.clear()
        
    return answer