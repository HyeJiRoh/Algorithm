def solution(arr):
    stk = [] 
    idx = 0 
    while idx < len(arr):
        if len(stk) == 0:
            stk.append(arr[idx])
        else:
            if stk[-1] == arr[idx]:
                stk.pop()
            elif stk[-1] != arr[idx]:
                stk.append(arr[idx])
        idx += 1 
        
    if len(stk) == 0:
        stk.append(-1)
        
    return stk 