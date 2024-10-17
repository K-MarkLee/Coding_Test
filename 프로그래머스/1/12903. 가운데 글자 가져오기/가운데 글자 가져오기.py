def solution(s):
    mid = len(s) // 2
    if len(s) % 2 == 0: 
        small = mid - 1
        return s[small : mid+1]
    else :
        return s[mid]