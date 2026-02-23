def solution(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    s1 = sum(arr1)
    s2 = sum(arr2)
    if l1 != l2:
        return ((l1 > l2) - (l2 > l1))
    return ((s1 > s2) - (s2 > s1))
        