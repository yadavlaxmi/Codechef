T=int(input())
for i in range(T):
    N,D=map(int,input().split())
    a=list(map(int,input().split()))
    b=0
    for i in a:
        if((i<=9)or(i>=80)):
            b+=1 
    c=N-b
    r=0
    j=0
    if(c%D==0):
        r=c//D 
    else:
        r=(c//D)+1 
    if(b%D==0):
        j=b//D
    else:
        j=(b//D)+1 
    r=r+j  
    print(r)