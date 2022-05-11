T=int(input())
for i in range(T):
    X,H=map(int,input().split())
    if X==H and X>0:
        print("YES")
    else:
        print("NO")