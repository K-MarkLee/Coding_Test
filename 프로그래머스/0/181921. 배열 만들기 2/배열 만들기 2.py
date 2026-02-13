from itertools import product
def solution(l, r):
    result = set()
    
    max_len= len(str(r))
    
    for i in range(1, max_len+1):
        for j in product(['0','5'], repeat = i):
            num = int("".join(j))
            
            if l <= num <=r :
                result.add(num)
    
    if not result:
        return [-1]
    else:
        return sorted(list(result))