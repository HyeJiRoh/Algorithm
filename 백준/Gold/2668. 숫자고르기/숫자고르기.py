N = int(input())			
arr = [0]				
for _ in range(N):
    arr.append(int(input()))
answer = set()			

def dfs(first, second, num):
    first.add(num)			
    second.add(arr[num])		
    if arr[num] in first:		
        if first == second:		
            answer.update(first)	
            return True
        return False
    return dfs(first, second, arr[num])	

for i in range(1, N+1):
    if i not in answer:			
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')