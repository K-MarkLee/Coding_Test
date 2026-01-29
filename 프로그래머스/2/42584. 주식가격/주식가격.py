from collections import deque
def solution(prices):
    result = []
    prices = deque(prices)
    while prices:
        current = prices.popleft()
        count = 0
        for i in prices:
            count += 1
            if i < current:
                break
        result.append(count)
    return result