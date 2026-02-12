def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        temp = min((i for i in arr[s:e+1] if i > k), default = -1)
        answer.append(temp)
    return answer