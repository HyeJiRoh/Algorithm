for idx in range(1, 11):
    n = int(input())
    arr = list(map(str, input().split("+")))
    
    result = 0

    for num in arr:
        result += int(num)

    print("#%d %d"%(idx, result))