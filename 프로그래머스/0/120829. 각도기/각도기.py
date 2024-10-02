def solution(angle):
    if angle <= 90:
        if angle == 90:
            return 2
        else:
            return 1
    else :
        if angle == 180:
            return 4
        else:
            return 3