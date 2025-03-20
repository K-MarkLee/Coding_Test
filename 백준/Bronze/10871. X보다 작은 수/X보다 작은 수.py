a,b=map(int,input().split())
c=list(map(int,input().split()))
c=[x for x in c if x < b]
for i in c:
    print(i,end=' ')