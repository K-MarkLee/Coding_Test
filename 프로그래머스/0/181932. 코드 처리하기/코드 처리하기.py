def solution(code):
    answer = []
    mode = 0
    for i, j in enumerate(code):
        if j == "1":
            mode = 1 - mode
        elif i % 2 == mode:
            answer.append(j)
    return "".join(answer) or "EMPTY"