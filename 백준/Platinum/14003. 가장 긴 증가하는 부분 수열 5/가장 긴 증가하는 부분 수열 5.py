import sys
import bisect
read = sys.stdin.readline

sequence_N = int(read().strip())
sequence_list = list(map(int, read().strip().split()))

record = [0] * (sequence_N)
dp = [sequence_list[0]]
record[0] = 1

for i in range(1, sequence_N):
    if dp[-1] < sequence_list[i]:
        dp.append(sequence_list[i])
        record[i] = len(dp)
    else:
        idx = bisect.bisect_left(dp, sequence_list[i])
        dp[idx] = sequence_list[i]
        record[i] = idx + 1

ans = []
find_dp = len(dp)
for i in range(len(record) - 1, -1, -1):
    if record[i] == find_dp:
        ans.append(sequence_list[i])
        find_dp -= 1

    if find_dp < 1:
        break

print(len(ans))
print(*ans[::-1])