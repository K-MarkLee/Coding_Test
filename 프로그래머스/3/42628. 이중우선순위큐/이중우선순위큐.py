import heapq
def solution(operations):
    sync = [0] * len(operations)
    max_heap = []
    min_heap = []
    
    for i, order in enumerate(operations):
        c , n = order.split()
        n = int(n)
        
        if c == "I":
            heapq.heappush(max_heap, [-n, i])
            heapq.heappush(min_heap, [n, i])
            sync[i] = 1
            
        elif c == "D":
            if n == 1:
                while max_heap and sync[max_heap[0][1]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    sync[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            elif n == -1:
                while min_heap and sync[min_heap[0][1]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    sync[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
                    
    while max_heap and sync[max_heap[0][1]] == 0:
        heapq.heappop(max_heap)
    while min_heap and sync[min_heap[0][1]] == 0:
        heapq.heappop(min_heap)

    if not max_heap and not min_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]