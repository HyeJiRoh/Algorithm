def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for idx in range(s, e+1):
            if arr[idx] > k:
                tmp.append(arr[idx])
        if not len(tmp) :
            answer.append(-1)
        else:
            answer.append(min(tmp))
    return answer