import sys
import heapq
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    num = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
        
    if left_heap and right_heap and -left_heap[0] > right_heap[0]:
        left_value = heapq.heappop(left_heap)
        right_value = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, right_value * -1)
        heapq.heappush(right_heap, left_value * -1)
        
    print(left_heap[0] * -1)