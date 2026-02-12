def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        temp = []
        for j in arr[s:e+1]:
            if j > k:
                temp.append(j)
        answer.append(min(temp) if temp else -1)
    return answer