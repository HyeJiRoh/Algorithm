def heap_sort(arr, n):
    global cnt
    build_min_heap(arr, n);
    
    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        cnt += 1
        if cnt == K:
            print(*arr[1:])
            exit()
        heapify(arr, 1, i - 1);

def build_min_heap(arr, n):
    for i in range(n // 2, 0, -1):
        heapify(arr, i, n)

def heapify(arr, k, n):
    global cnt
    left, right = 2 * k, 2 * k + 1
    if right <= n:
        smaller = left if arr[left] < arr[right] else right
    elif left <= n:
        smaller = left
    else:
        return

    if arr[smaller] < arr[k]:
        arr[k], arr[smaller] = arr[smaller], arr[k]
        cnt += 1
        if cnt == K:
            print(*arr[1:])
            exit()
        heapify(arr, smaller, n);

N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
cnt = 0
heap_sort(arr, N)
print(-1)