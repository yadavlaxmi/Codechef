T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if X>Y:
        print("SECOND")
    if Y>X:
        print("FIRST")
    if Y==X:
        print("ANY")