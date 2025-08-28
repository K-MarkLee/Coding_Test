import sys

while True:
    n = int(sys.stdin.readline().strip())
    factors = []
    
    if n == -1:
        break
    
    for i in range(1,n):
        if n % i == 0:
            factors.append(i)
    
    if sum(factors) == n :
        print(f"{n} = " + " + ".join(str(j) for j in factors))
    else :
        print(f"{n} is NOT perfect.")