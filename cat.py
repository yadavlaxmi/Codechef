t = int(input())
while t:
    c,d,l = map(int,input().split())
    total = (c+d)*4
    mini = max(0,c-d*2)
    if(total>=l and l%4==0 and (d+mini)*4<=l):
        print("yes")
    else:
        print("no")
    t-=1
# dogs/cats legs