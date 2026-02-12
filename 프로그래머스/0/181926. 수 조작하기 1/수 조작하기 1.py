def solution(n, control):
    answer = n
    c_dict = {"w":1, "s":-1, "d":10, "a":-10}
    for i in control:
        answer += c_dict[i]
    return answer