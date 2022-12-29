money = int(input())
exchange = 1000-money
cnt = 0

# 500 100 50 10 5 1

while exchange != 0 :
    if exchange >= 500 :
        cnt += 1
        exchange -= 500
    elif exchange >= 100 and exchange < 500:
        cnt += 1
        exchange -= 100
    elif exchange >= 50 and exchange < 100:
        cnt += 1
        exchange -= 50
    elif exchange >= 10 and exchange < 50:
        cnt += 1
        exchange -= 10
    elif exchange >= 5 and exchange < 10:
        cnt += 1
        exchange -= 5
    else:
        cnt += 1
        exchange -= 1

print(cnt)