T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if Y in range (X,X+200+1):
        print("YES")
    else:
        print("NO")