from itertools import permutations
def solution(k, dungeons):
    max_count = 0
    
    for order in permutations(dungeons, len(dungeons)):
        count = 0
        current = k
        
        for i in order:
            least = i[0]
            reduce = i[1]
            
            if current >= least:
                count += 1
                current -= reduce
            else:
                break
        max_count = max(count, max_count)
    return max_count