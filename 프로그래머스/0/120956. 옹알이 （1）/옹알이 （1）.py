def solution(babbling):
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya","0").replace("ye","0").replace("woo","0").replace("ma","0")
    
    answer = [i for i in babbling if i.isdigit()]
    if not answer:
        return 0
    return len(answer)