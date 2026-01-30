def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(3, total):
        n = total // i
        if total % i == 0 and i >= n:
            if (n-2)* (i-2) == yellow:
                return [i , n]