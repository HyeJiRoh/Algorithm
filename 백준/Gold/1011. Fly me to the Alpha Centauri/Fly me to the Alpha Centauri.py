T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    distance = y - x
    tmp_move = 0
    cnt = 0
    move = 0

    while tmp_move < distance:
        cnt += 1
        if cnt % 2 != 0 :
            move += 1

        tmp_move += move

    print(cnt) 