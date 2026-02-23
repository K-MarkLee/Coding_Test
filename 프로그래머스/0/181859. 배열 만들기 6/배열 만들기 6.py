def solution(arr):
    answer = []
    for i in range(len(arr)):
        if answer and answer[-1] == arr[i]:
            del answer[-1:]
        else:
            answer.append(arr[i])
    return answer or [-1]