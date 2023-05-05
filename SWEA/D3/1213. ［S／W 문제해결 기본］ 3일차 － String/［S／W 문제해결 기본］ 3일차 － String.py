for idx in range(1, 11):
    n = int(input())
    cnt = 0

    base = input().strip()
    str = input().strip()

    cnt = str.count(base)
    print("#%d %d" %(idx, cnt))