import sys
input = sys.stdin.readline

K = int(input())

for i in range(K) :
    arr = list(map(int, input().strip().split()))
    N = arr[0]
    score = arr[1:]
    score.sort(reverse=True)
    gap = 0
    base = 0

    for k in range(1, len(score)) :
        gap = score[k-1]-score[k]
        if gap > base :
            base = gap

    print("Class %d"%(i+1))
    print("Max %d, Min %d, Largest gap %d"%(score[0], score[-1], base))
