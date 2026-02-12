def solution(code):
    mode = 0 
    answer = ''
    for j, i in enumerate(code):
        if i == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if mode == 0 and j % 2 == 0:
                answer += i
            if mode == 1 and j % 2 != 0:
                answer += i
    return answer if answer else "EMPTY"