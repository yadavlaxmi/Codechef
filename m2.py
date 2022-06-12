n=int(input())
for i in range(n):
    X,Y=map(int,input().split())
    if X<Y:
        print("FIRST")
    elif X==Y:
        print("ANY")
    elif X>Y:
        print("SECOND")
