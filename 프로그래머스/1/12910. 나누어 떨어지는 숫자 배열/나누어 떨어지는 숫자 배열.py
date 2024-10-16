def solution(arr, divisor):
    result = [x for x in arr if x % divisor == 0]
    if not result:
        return [-1]
    return sorted(result)