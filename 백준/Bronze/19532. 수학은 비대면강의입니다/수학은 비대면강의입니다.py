import sys
a,b,c,d,e,f = map(int,sys.stdin.read().strip().split())

print(f"{((c*e)-(b*f))//((e*a)-(d*b))} {((f*a)-(d*c))//((e*a)-(d*b))}")