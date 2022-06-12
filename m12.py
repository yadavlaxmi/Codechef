import sys
y = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
c = 0
for i in range(y[0]):
    x = int(sys.stdin.readline().rstrip('\n'))
    if x%y[1] == 0:
        c += 1
print(c)
