def solution(order):
    n = 0
    for i in order:
        if "latte" in i:
            n+=1
    return ((len(order)-n) * 4500 + n * 5000)