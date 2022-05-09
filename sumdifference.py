def differenceofSum(n,m):
    i=1
    sum1=0
    sum2=0
    difference=0
    while i<=(m):
        if i%n==0:
            sum1=sum1+i
        else:
            sum2=sum2+i
        i=i+1
    difference=sum2-sum1
    return(difference)
n=int(input())
m=int(input())
print(differenceofSum(n,m))
# SUM DIFFERNCE
