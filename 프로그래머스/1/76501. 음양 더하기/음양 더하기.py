def solution(absolutes, signs):
    total = 0
    for i in range(len(signs)):
        if signs[i] == True:
            total += absolutes[i]
        elif signs[i] == False:
            total -= absolutes[i]
    return total

        
    