def solution(numbers):
    result = list(map(str, numbers))
    result.sort(key=lambda x : x*3, reverse=True)
    if result[0] == "0":
        return "0"
    return ''.join(result)