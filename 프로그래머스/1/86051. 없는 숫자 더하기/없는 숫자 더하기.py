import numpy as np
def solution(numbers):
    all = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
    num = np.array(numbers)
    return sum(set(all.tolist()) - set(num.tolist()))