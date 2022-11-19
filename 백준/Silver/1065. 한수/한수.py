def hansu(num) :
    count = 0
    for i in range(1, num+1):
        nl = list(map(int,str(i)))
        if i < 100:
            count += 1
        elif nl[0]-nl[1] == nl[1]-nl[2]:
            count += 1 
    return count

num = int(input())
print(hansu(num))