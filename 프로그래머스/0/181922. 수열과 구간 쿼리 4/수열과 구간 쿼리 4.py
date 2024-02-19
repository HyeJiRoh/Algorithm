def solution(arr, queries):
    for s, e, k in queries:
        for idx in range(s, e+1):
            if idx % k == 0:
                arr[idx] += 1
    return arr