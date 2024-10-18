def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum += price * i
    if sum > money :
        total = sum - money
        return total
    else :
        return 0