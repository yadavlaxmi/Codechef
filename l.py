text = input("enter the string")
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newtext = ""
vowel=[]
c=0
textlen = len(text)
for i in range(textlen):
    
    if text[i] not in vow:
        newtext = newtext + text[i]
    if text[i] in vow:
        c=c+1
        vowel.append(text[i])
text = newtext
print(text)
print(vowel)
print("total vowel",c)