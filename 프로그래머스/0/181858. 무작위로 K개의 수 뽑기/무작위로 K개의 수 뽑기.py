def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer and len(answer) != k:
            answer.extend([i])
    return answer + [-1] * (k - len(answer))