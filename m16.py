T=int(input())
for i in range(T):
    X,Y,Z=list(map(int,input().split()))
    a=X*5
    b=Y*10
    sum=a+b
    c=sum//Z
    print(c)
    #  chocolate