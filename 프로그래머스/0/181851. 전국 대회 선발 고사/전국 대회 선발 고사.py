def solution(rank, attendance):
    n = len(rank)
    answer =0
    rank_list = []

    for i in range(n):
        if attendance[i]:
            rank_list.append([rank[i], i])

    rank_list.sort(key = lambda v : v[0])

    return 10000 * rank_list[0][1] + 100 * rank_list[1][1] + rank_list[2][1]