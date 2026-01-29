import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    count = 0
    i = 0
    now = 0
    heap = []
    
    while count < len(jobs):
        while i < len(jobs) and jobs[i][0] <= now:
            heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
            i += 1
        
        if len(heap) > 0:
            long, start = heapq.heappop(heap)
            
            now += long
            count += 1
            answer += (now - start)
        else:
            now = jobs[i][0]
    
    return answer // len(jobs)
            