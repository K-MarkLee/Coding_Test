import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        count += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if second == 0:
            return -1
        heapq.heappush(scoville, first + second * 2)
    return count