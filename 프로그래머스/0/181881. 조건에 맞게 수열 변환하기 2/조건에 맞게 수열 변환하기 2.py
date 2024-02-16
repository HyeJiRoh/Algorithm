def solution(arr):
    x = 0
    tmp = list(arr)
    
    while True:
        for idx in range(len(tmp)):
            if tmp[idx] >= 50 and tmp[idx]%2==0:
                tmp[idx] = tmp[idx]//2
            elif tmp[idx] < 50 and tmp[idx]%2==1:
                tmp[idx] = tmp[idx]*2+1
    
        if tmp == arr:
            return x
        else:
            arr = list(tmp)
            x += 1