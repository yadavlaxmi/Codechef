X=int(input())
for i in range(X):
    T,H=map(int,input().split())
    if T>=H:
        print("YES")
    else:
        print("NO")
