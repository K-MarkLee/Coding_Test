a=int(input())
b=int(input())
b100=b//100
b10=(b%100)//10
b1=b%10
print(f"{a*b1}\n{a*b10}\n{a*b100}\n{a*b}")