def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    
    for line in arr1:
        bin_arr1.append(bin(line)[2:].zfill(n))
    
    for line in arr2:
        bin_arr2.append(bin(line)[2:].zfill(n))
    
    for i in range(n):
        tmp = ""
        for j in range(n):
            if bin_arr1[i][j] == '1' or bin_arr2[i][j] == '1':
                tmp += "#"
            elif bin_arr1[i][j] == '0' and bin_arr2[i][j] == '0':
                tmp += " "
        answer.append(tmp)
    
    return answer