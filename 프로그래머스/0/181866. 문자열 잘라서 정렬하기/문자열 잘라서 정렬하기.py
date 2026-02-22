def solution(myString):

    return sorted(i for i in myString.strip().split("x") if i != "")