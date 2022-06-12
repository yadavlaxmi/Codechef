T = int(input())
while T>0:
    a,b,c = map(int,input().split())
    if (a>b and a<c) or (a>c and a<b):
        print(a)
    elif (b>c and b<a) or (b>a and b<c):
        print(b)
    else:
        print(c)
    T-=1
