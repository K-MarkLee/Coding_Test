def solution(priorities, location):
    result = [(i,j) for i,j in enumerate(priorities) ]
    answer = 0
    
    while result:
        current = result.pop(0)
        current_priority = current[1]
        current_index = current[0]
        
        if any(current_priority < i[1] for i in result):
            result.append(current)
        else:
            answer += 1
            
            if location == current_index:
                return answer
        