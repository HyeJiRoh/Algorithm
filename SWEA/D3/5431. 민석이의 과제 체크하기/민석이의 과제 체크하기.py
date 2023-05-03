T = int(input())

for idx in range(1, T + 1):
    n, k = map(int, input().split())
    student = list(map(int, input().split()))
    result = []

    student.sort()
    
    for num in range(1, n + 1):
        if num not in student:
            result.append(num)
    
    print("#%d"%idx, end = " ")
    
    for i in result:
        print(i, end = " ")
    
    print()