
# def FindSumOfRemainders(n,div):
i=1
rem=0
sum=0
while i<=12:
  if i%4==rem:
    sum=sum+rem
    rem=rem+1
  i=i+1
  print(sum)
# print(FindSumOfRemainders(12,4))/