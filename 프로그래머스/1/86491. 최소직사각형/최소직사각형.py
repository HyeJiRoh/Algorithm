def solution(sizes):
    answer = 0
    left_max, right_max = 0, 0
    for idx in range(len(sizes)):
        if sizes[idx][0] < sizes[idx][1]:
            sizes[idx][0], sizes[idx][1] = sizes[idx][1], sizes[idx][0]
        if sizes[idx][0] > left_max:
            left_max = sizes[idx][0]
        if sizes[idx][1] > right_max:
            right_max = sizes[idx][1]
    answer = left_max * right_max
    return answer