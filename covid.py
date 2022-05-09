n=int(input())
for i in range(n):
    N,K,X,Y=map(int,input().split())
    M=X
    while X<=N:
        if X==Y:
           print("YES")
           break
        X=(X+K)%N
        if X==M:
           print("NO")
           break
    