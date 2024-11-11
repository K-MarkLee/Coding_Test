def solution(n):
    first, second, last = 0, 1, 2
    for i in range (n-1):
        last = first + second
        first = second
        second = last
    return last % 1234567