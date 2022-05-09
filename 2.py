def SumOfNumbers(l,n,k):
    k = int(input())
    n = int(input())
    l = []

for i in range(0, n):
    p = int(input())
    l.append(p)
    l.sort()
    sum=l[0]+l[-1]
        return(sum)
result = SumOfNumbers(l,n,k)
print(result)