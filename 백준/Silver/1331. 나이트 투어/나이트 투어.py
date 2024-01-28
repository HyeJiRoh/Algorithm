import sys
input = sys.stdin.readline

visited = []
answer = "Valid"
for i in range(36):
    if i == 0: 
        start = input().rstrip()
        pre = start
    elif i < 35:
        now = input().rstrip()
        if ((abs(ord(pre[0]) - ord(now[0])) ==1 and abs(int(pre[1])-int(now[1])) == 2) or (abs(ord(pre[0]) - ord(now[0])) ==2 and abs(int(pre[1])-int(now[1])) == 1)) and now not in visited:
            pass
        else:   
            answer = "Invalid"
        visited.append(now) # 방문리스트에 삽입
        pre = now
    else:
        now = input().rstrip()
        if ((abs(ord(now[0]) - ord(start[0])) ==1 and abs(int(now[1])-int(start[1])) == 2) or (abs(ord(now[0]) - ord(start[0])) ==2 and abs(int(now[1])-int(start[1])) == 1)) and now not in visited:
            pass
        else:
            answer = "Invalid"

print(answer)