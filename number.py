def positiveinteger(m,n):
    i=m
    sum1=0
    while i<=n:
        if i%3==0 and i%5==0:
            sum1=sum1+i
        i=i+1    
    return(sum1)
m=int(input())
n=int(input())
print(positiveinteger(m,n))
# NUMBER