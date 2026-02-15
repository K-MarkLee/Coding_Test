def solution(my_string, alp):
    answer = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == alp:
            answer[i] = my_string[i].upper()
    return "".join(answer)