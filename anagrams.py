Input1=input()  
Input2=input()
def Anagrams():
    i=0
    c=''
    while i<len(Input1):
        if Input1[i] in Input2:
            c=c+Input1[i]
        i=i+1
    if c==Input1:
        return 'YES'
    else:
        return 'NO'  
print(Anagrams())
# ANAGRAMS