from itertools import product
def solution(l, r):
    result = set()
    
    length = len(str(r))
    
    for i in range(1, length+1):
        for j in product(['0','5'], repeat = length):
            num = int("".join(j))
            if l <= num <= r:
                result.add(num)
    
    if result:
        return sorted(list(result))
    else:
        return [-1]
            