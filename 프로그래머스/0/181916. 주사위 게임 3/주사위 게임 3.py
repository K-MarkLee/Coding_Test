def solution(a, b, c, d):
    arr = [a,b,c,d]
    arr_set = set(arr)
    length = len(arr_set)  
    sum_arr = sum(arr)
    sum_set = sum(arr_set)

    if length == 1:
        return 1111 * a
    
    elif length == 2:
        if 2 * sum_set == sum_arr:
            p,q = list(arr_set)
            return (p+q) * abs(p-q)
        
        else:
            for i in arr_set:
                if arr.count(i) == 3:
                    p = i
                else:
                    q = i
            return (10 * p + q) ** 2

    elif length == 3:
        i = sum_arr- sum_set
        p,q,r = list(arr_set)
        return (p*q*r) // i
    
    else:
        return min(arr)    