n = int(input())

for idx in range(1, n+1):
    init = list(input())
    tmp = ['0'] * len(init)
    cnt = 0

    while True:
        if init == tmp:
            break

        for i in range(len(init)):
            if init[i] != tmp[i]:
                for j in range(i, len(tmp)):
                    tmp[j] = init[i]
                cnt += 1

    print("#%d %d"%(idx, cnt))