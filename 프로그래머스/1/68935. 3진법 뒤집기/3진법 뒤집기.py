def solution(n):
    reversed_ternary = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        reversed_ternary = str(remainder) + reversed_ternary
    answer = int(reversed_ternary[::-1], 3)
    return answer