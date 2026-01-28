def solution(s):
    open = 1
    start = s[0]
    for i in range(1,len(s)):
        if open < 0:
            return False
        if s[i] == "(":
            open +=1
        elif s[i] == ")":
            open -= 1
    return True if open == 0 else False
        