
a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=sum(c)
    if d%2==0:
        print("0")
    else:
        d=0
        for i in range(b):
            if c[i]==2:
                d+=1
        if d!=0:
            print("1")
        else:
            print("-1")
