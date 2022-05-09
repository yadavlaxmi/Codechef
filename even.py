testcase=int(input())
for i in range (testcase):
    a,b=list(map(int,input().split()))
    a_even=a//2
    a_odd=a-a_even
    b_even=b//2
    b_odd=b-b_even
    pair=(a_even*b_even)+(a_odd*b_odd)
    print(pair)