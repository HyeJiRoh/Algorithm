n, m = map(int, input().split())
s = list(map(int ,input().split()))
q = [i for i in range(1, n + 1)]
cnt = 0
for i in range(m):
    q_len = len(q)
    q_index = q.index(s[i])
    if q_index < q_len - q_index:
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                cnt += 1
    else:
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                cnt += 1
print(cnt)