for _ in range(int(input())):
    n=int(input())
    x=list(map(str,input().split()))
    flag=1
    if(x[n-1]=="cookie"):
        print("NO")
    else:
        for j in range(0,n-1):
            if(x[j]=="cookie" and x[j+1]!="milk"):
                print("NO")
                flag=0
                break
        if(flag!=0):
            print("YES")
        