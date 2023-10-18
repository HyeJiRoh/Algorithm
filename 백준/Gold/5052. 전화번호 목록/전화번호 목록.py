T = int(input())

for _ in range(T):
    n = int(input())
    flag = True
    phone = [input() for _ in range(n)]

    phone.sort()

    for i in range(n-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            flag = False
            break
        
    if flag:
        print("YES")
    else:
        print("NO")
