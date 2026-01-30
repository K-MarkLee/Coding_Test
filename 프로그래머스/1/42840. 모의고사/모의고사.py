def solution(answers):
    l1 = [1,2,3,4,5]
    l2 = [2,1,2,3,2,4,2,5]
    l3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == l1[i%5]:
            score[0] += 1
        if answers[i] == l2[i%8]:
            score[1] += 1
        if answers[i] == l3[i%10]:
            score[2] += 1
    max_score = max(score)
    result = []
    for i, j in enumerate(score):
        if j == max_score:
            result.append(i+1)
    return result
    
        