from itertools import permutations
def solution(numbers):
    numbers = list(numbers)
    com = set()
    
    for i in range(len(numbers)):
        for j in permutations(numbers, i+1):
            com.add(int(''.join(j)))
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    result = 0
    for i in com:
        if is_prime(i):
            result += 1
    return result
    