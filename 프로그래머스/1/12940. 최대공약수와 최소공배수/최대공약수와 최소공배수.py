import numpy as np
def solution(n, m):
    gcd = np.gcd(n,m).item()
    lcm = np.lcm(n,m).item()
    result = [gcd,lcm]
    return result