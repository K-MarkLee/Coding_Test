from math import gcd
def solution(arr):
    for i in range (0,len(arr)-1):
        arr[i+1] = arr[i] * arr[i+1] // gcd(arr[i], arr[i+1])
    return arr[i+1]
    