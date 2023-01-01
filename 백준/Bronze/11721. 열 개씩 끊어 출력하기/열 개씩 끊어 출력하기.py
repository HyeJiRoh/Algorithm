str = list(input())
for i in range(len(str)//10+1) :
    i*=10
    for k in str[i:i+10] :
        print(k, end = "")
    print("")