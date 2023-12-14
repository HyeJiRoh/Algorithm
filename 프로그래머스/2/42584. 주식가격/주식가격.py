from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        cur_price = prices.popleft()
        cnt = 0
        for price in prices:
            cnt += 1
            if cur_price > price:
                break
        answer.append(cnt)
    
    return answer