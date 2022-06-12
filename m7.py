T=int(input())
for _ in range(T):
    X, Y = map(int,input().split())
    b=0
    while X < Y or X > Y:
        if X <= Y:
            b+=1
            X+=1
        else:
            b+=1
            X-=1
    print(b)