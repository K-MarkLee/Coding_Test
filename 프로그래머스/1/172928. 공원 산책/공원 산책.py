def solution(park, routes):
    h = len(park)
    w = len(park[0])
    
    x, y = next((i, j) for i, row in enumerate(park) for j, char in enumerate(row) if char == 'S')
    
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    for route in routes:
        d,n = route.split()
        dx,dy = directions[d]
        nx,ny = x,y
        
        for _ in range(int(n)):
            nx += dx
            ny += dy
            
            if not (0 <= nx <h and 0 <= ny < w) or park[nx][ny] == 'X':
                break
        else:
            x,y = nx, ny
    
    return [x,y]