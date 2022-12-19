arr = list(map(int, input().split()))
count = 0

for i in range(1, len(arr)) :
    if arr[i]-arr[i-1] == 1 :
        count += 1
    elif arr[i]-arr[i-1] == -1 :
        count -= 1

if count == 7 :
    print("ascending")
elif count == -7 :
    print("descending")
else :
    print("mixed")