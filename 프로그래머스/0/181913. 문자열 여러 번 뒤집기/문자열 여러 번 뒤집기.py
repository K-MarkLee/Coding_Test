def solution(my_string, queries):
    li = list(my_string)
    for s,e in queries:
        li[s:e+1] = li[s:e+1][::-1]
    return "".join(li)