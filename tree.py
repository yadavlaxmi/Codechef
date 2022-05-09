for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    s.discard(0)
    print(len(s))
  # tree
  t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=set(a)
    if 0 in s:
        print(len(s)-1)
    else:
        print(len(s))