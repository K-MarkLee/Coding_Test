def solution(name):
    answer = 0
    n = len(name)
    min_move = n - 1
    
    for i, j in enumerate(name):
        up = ord(j) - ord('A')
        down = ord('Z') - ord(j) + 1
        
        answer += min(up, down)
        
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        
        path1 = i * 2 + (n - next)
        path2 = i + (n - next) * 2
        min_move = min(path1, path2, min_move)
    return answer + min_move